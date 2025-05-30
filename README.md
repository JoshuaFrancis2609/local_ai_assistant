# Local Privacy-First AI Assistant

This project is my attempt to create a lightweight local-only (after install) AI assistant designed to answer privacy, security, and general knowledge questions. It runs fully offline after setup using local LLM (Large Language Model). Basically, no internet connection required after install.

## Features

- Private and secure: No external API calls after setup
- Lightweight: Hopefully can run on laptop or maybe tablets
- Expandable: Might try to create future features like encrypted notes and offline scheduling

## Requirements

- Python (I created this using 3.8 I believe so that or better)
- Ollama installed
- Enough disk space for local LLM models (searching online it looks like ~5GB for Phi-2)

## Setup (MVP Version)

- Install LLM [going with Ollama]
- Download the Phi-2 model
- Clone this repository and run the test script
``` bash
git clone https://github.com/JoshuaFrancis2609/local_ai_assistant.git
cd local_ai_assistant
pip install -r requirements.txt
python local_ai_assistant_test.py
```

## License

This project is licensed under the MIT License