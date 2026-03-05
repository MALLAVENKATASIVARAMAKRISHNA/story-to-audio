import os
import requests
import base64
from dotenv import load_dotenv
from pydub import AudioSegment
import io

def chunk_text(text, max_chars=450):
    """Splits text into chunks of roughly max_chars, preferably at sentence boundaries."""
    chunks = []
    current_chunk = ""
    
    # Split by common Telugu/English punctuation
    import re
    sentences = re.split('([.।!?])', text)
    
    temp_sentence = ""
    for part in sentences:
        temp_sentence += part
        if any(p in part for p in ".।!?"):
            if len(current_chunk) + len(temp_sentence) <= max_chars:
                current_chunk += temp_sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = temp_sentence
            temp_sentence = ""
            
    if temp_sentence:
        current_chunk += temp_sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def main():
    load_dotenv()
    api_key = os.getenv("SAVRAM_API_KEY")

    if not api_key or api_key == "your_api_key_here":
        print("Error: Please set your SAVRAM_API_KEY in the .env file.")
        return

    try:
        with open("story.txt", "r", encoding="utf-8") as f:
            story_text = f.read().strip()
    except FileNotFoundError:
        print("Error: story.txt not found.")
        return

    if not story_text:
        print("Error: story.txt is empty.")
        return

    chunks = chunk_text(story_text)
    print(f"Split story into {len(chunks)} chunks. Processing...")

    output_dir = "audios"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "output.mp3")
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }

    combined_audio = AudioSegment.empty()
    # Add a short silence (500ms) to be used between chunks
    silence = AudioSegment.silent(duration=500)

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)} ({len(chunk)} characters)...")
        
        payload = {
            "inputs": [chunk],
            "target_language_code": "te-IN",
            "speaker": "kavya",
            "pace": 1.0,
            "model": "bulbul:v3",
            "audio_format": "wav"  # Using WAV for better compatibility during merging
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if 'audios' in data and len(data['audios']) > 0:
                    audio_bytes = base64.b64decode(data['audios'][0])
                    # Load as WAV
                    segment = AudioSegment.from_wav(io.BytesIO(audio_bytes))
                    combined_audio += segment + silence
                else:
                    print(f"Error in chunk {i+1}: 'audios' key missing.")
            else:
                print(f"Error in chunk {i+1}: API returned {response.status_code}")
                print(response.text)
                return
        except Exception as e:
            print(f"An error occurred in chunk {i+1}: {e}")
            return

    print(f"Exporting final audio to {output_file}...")
    # Export the combined WAV data as an MP3 file
    combined_audio.export(output_file, format="mp3", bitrate="128k")
    print("Success!")

if __name__ == "__main__":
    main()
