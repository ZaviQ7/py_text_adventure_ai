# Python AI Text Adventure

This is a fully offline, AI-enhanced text adventure game built in Python. It features a modular architecture, a branching narrative, a player inventory system, and an optional AI storyteller powered by a local GPT-2 model. The game can be played in a modern Tkinter GUI or a classic command-line interface.

![Screenshot 2025-06-26 190141](https://github.com/user-attachments/assets/2771420e-e684-4248-8f09-a57984bdb4ba)
 

## Features

- **Offline First**: After a one-time setup, the game runs entirely without an internet connection.
- **AI-Powered Narration**: Certain scenes use a local GPT-2 model to generate dynamic and unique descriptions, adding replayability.
- **Branching Narrative**: Your decisions matter and lead to different outcomes and story paths.
- **Inventory System**: Find and use items to solve puzzles and unlock new areas.
- **Dual Interface**: Choose between a user-friendly GUI (`--mode gui`) or a traditional terminal experience (`--mode cli`).
- **Modular Design**: The code is cleanly separated into a game engine, story data, AI module, and UI, making it easy to extend or modify.

## Setup and Installation

Follow these steps to get the game running on your local machine. This project is compatible with Windows, macOS, and Linux.

**Prerequisites:**
- Python 3.7+
- `pip` (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/py_text_adventure_ai.git
cd py_text_adventure_ai
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```
**Note for NVIDIA GPU Users**: For significantly better performance with the AI model, install the CUDA-enabled version of PyTorch. Find the correct command for your system on the [PyTorch website](https://pytorch.org/get-started/locally/). For example:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

### Step 4: Download the AI Model (One-Time Setup)

To enable the AI features offline, you must first download the GPT-2 model. Run the included script:

```bash
python download_model.py
```
This will download the model (approx. 500MB) and save it to a local `models/gpt2` directory. This directory is included in `.gitignore` and will not be committed to the repository.

## How to Play

Once the setup is complete, you can run the game from the root directory of the project.

### To run in GUI mode (Default):
```bash
python -m src.main
# or
python -m src.main --mode gui
```

### To run in Command-Line (CLI) mode:
```bash
python -m src.main --mode cli
```

Enjoy your adventure!
