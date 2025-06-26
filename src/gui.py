# src/gui.py

import tkinter as tk
from tkinter import scrolledtext, messagebox

class GameGUI(tk.Tk):
    """A Tkinter-based GUI for the text adventure game."""
    def __init__(self, game_engine):
        super().__init__()
        self.game_engine = game_engine
        self.title("Python AI Text Adventure")
        self.geometry("800x600")
        self.configure(bg="#2E2E2E")

        self._setup_widgets()
        self.update_ui()

    def _setup_widgets(self):
        """Creates and places the widgets in the window."""
        # Main text display
        self.text_display = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Helvetica", 12),
            bg="#1C1C1C", fg="#E0E0E0", insertbackground="#E0E0E0",
            borderwidth=0, highlightthickness=0
        )
        self.text_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_display.config(state=tk.DISABLED)

        # Inventory display
        self.inventory_label = tk.Label(
            self, text="Inventory:", font=("Helvetica", 10, "bold"),
            bg="#2E2E2E", fg="#A0A0A0"
        )
        self.inventory_label.pack(pady=(0, 5))

        # Frame for choice buttons
        self.choices_frame = tk.Frame(self, bg="#2E2E2E")
        self.choices_frame.pack(padx=10, pady=10, fill=tk.X)

    def update_ui(self):
        """Updates the UI with the current game state."""
        state = self.game_engine.get_current_state()

        # Update main text
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, state["description"])
        self.text_display.config(state=tk.DISABLED)

        # Update inventory
        inventory_text = "Inventory: " + (", ".join(state["inventory"]) if state["inventory"] else "Empty")
        self.inventory_label.config(text=inventory_text)

        # Clear old choice buttons
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

        # Create new choice buttons
        if state["is_game_over"]:
            self.show_game_over()
        else:
            for choice_text in state["choices"]:
                button = tk.Button(
                    self.choices_frame, text=choice_text,
                    command=lambda c=choice_text: self.handle_choice(c),
                    bg="#4A4A4A", fg="white", font=("Helvetica", 10),
                    relief=tk.FLAT, padx=10, pady=5
                )
                button.pack(fill=tk.X, pady=2)

    def handle_choice(self, choice_text):
        """Processes a player's choice and updates the UI."""
        self.game_engine.process_input(choice_text)
        self.update_ui()

    def show_game_over(self):
        """Displays a game over message."""
        play_again = messagebox.askyesno(
            "Game Over",
            "Your adventure has ended. Would you like to play again?"
        )
        if play_again:
            self.game_engine.__init__() # Reset the engine
            self.update_ui()
        else:
            self.quit()