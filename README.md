# Story to Audio Converter

This project contains a Python script to convert Telugu story text files into audio using the `savram.ai` API.

## Project Structure

- `.env`: Stores your `savram.ai` API key.
- `requirements.txt`: Lists Python dependencies.
- `main.py`: The main script for text-to-audio conversion.
- `story.txt`: Input file for the Telugu story.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd story-to-audio
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up API Key:**
    Create a `.env` file in the project root and add your `savram.ai` API key:
    ```
    SAVRAM_API_KEY="your_savram_api_key_here"
    ```

## Examples

### Example 1: కోతి మరియు మొసలి (The Monkey and the Crocodile)

**Story Text:**
> కోతి మరియు మొసలి
> ఒకానొకప్పుడు ఒక పెద్ద నది తీరాన ఒక పెద్ద నేరేడు చెట్టు ఉండేది. ఆ చెట్టుపై ఒక తెలివైన కోతి నివసించేది. ఆ నేరేడు పండ్లు చాలా తీపిగా ఉండేవి. కోతి ప్రతిరోజూ ఆ పండ్లను తింటూ చాలా సంతోషంగా ఉండేది... (వెనక్కి వెళ్లి తన ప్రాణాలను కాపాడుకుంది).

**Generated Audio:**
<audio controls>
  <source src="audios/output.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

---

### Example 2: సింహం మరియు ఎలుక (The Lion and the Mouse)

**Story Text:**
> ఒక అడవిలో ఒక సింహం నిద్రపోతుండగా, ఒక చిన్న ఎలుక దానిపై ఆడుకోవడం మొదలుపెట్టింది. సింహం కోపంతో ఎలుకను పట్టుకుంది. ఎలుక ప్రాధేయపడటంతో సింహం దాన్ని వదిలేసింది. కొద్దిరోజుల తర్వాత సింహం వేటగాడి వలలో చిక్కుకోగా, ఎలుక ఆ వలను కొరికి సింహాన్ని కాపాడింది.

**Generated Audio:**
*(Run the script with this text to generate the audio)*

## Usage

1.  Place your Telugu story text (max 200 words) in `story.txt`.
2.  Run the script:
    ```bash
    python main.py
    ```
    The generated audio will be saved as `output.mp3`.

## Disclaimer

This script relies on the `savram.ai` API. Please ensure you have an active API key and adhere to their terms of service.
