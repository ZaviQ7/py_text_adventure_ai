# src/player.py

class Player:
    """Represents the player and their inventory."""
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        """Adds an item to the player's inventory."""
        if item not in self.inventory:
            self.inventory.append(item)
            return f"You found a {item}!"
        return ""

    def has_item(self, item):
        """Checks if the player has a specific item."""
        return item in self.inventory