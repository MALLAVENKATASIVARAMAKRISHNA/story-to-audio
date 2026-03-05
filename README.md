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

## Usage

1.  Place your Telugu story text (max 200 words) in `story.txt`.
2.  Run the script:
    ```bash
    python main.py
    ```
    The generated audio will be saved as `output.mp3`.

## Disclaimer

This script relies on the `savram.ai` API. Please ensure you have an active API key and adhere to their terms of service.
