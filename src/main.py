# src/main.py

import argparse
import textwrap
from src.game_engine import GameEngine
from src.gui import GameGUI

def run_cli():
    """Runs the game in the command-line interface."""
    engine = GameEngine()
    print("\n--- Welcome to Python AI Text Adventure ---")

    while True:
        state = engine.get_current_state()
        
        # Print description
        print("\n" + "="*80)
        print(textwrap.fill(state["description"], width=80))
        print("="*80)

        # Print inventory
        inventory_text = ", ".join(state["inventory"]) if state["inventory"] else "Empty"
        print(f"Inventory: {inventory_text}\n")

        if state["is_game_over"]:
            print("--- GAME OVER ---")
            break

        # Get player choice
        choices = list(state["choices"].keys())
        for i, choice in enumerate(choices):
            print(f"{i + 1}: {choice}")

        try:
            player_input = input("\nWhat do you do? (Enter a number): ")
            choice_index = int(player_input) - 1
            if 0 <= choice_index < len(choices):
                chosen_text = choices[choice_index]
                engine.process_input(chosen_text)
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to your choice.")

def run_gui():
    """Runs the game in the Tkinter GUI."""
    engine = GameEngine()
    app = GameGUI(engine)
    app.mainloop()

def main():
    """Parses arguments and starts the game in the chosen mode."""
    parser = argparse.ArgumentParser(description="An offline AI-powered text adventure game.")
    parser.add_argument(
        '--mode',
        choices=['gui', 'cli'],
        default='gui',
        help="The interface to run the game in (default: gui)"
    )
    args = parser.parse_args()

    if args.mode == 'cli':
        run_cli()
    else:
        run_gui()

if __name__ == "__main__":
    main()