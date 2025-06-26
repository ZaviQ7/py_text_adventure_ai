# src/game_engine.py

from src.player import Player
from src.story import STORY_DATA
from src.ai_engine import AIEngine

class GameEngine:
    """Manages the game state, narrative, and player interactions."""
    def __init__(self):
        self.player = Player()
        self.ai_engine = AIEngine()
        self.story = STORY_DATA
        self.current_scene_id = 'START'
        self.message = "" # For messages like "Item found!"

    def get_current_state(self):
        """Returns all necessary info for the UI to render the current state."""
        scene = self.story.get(self.current_scene_id, {})
        description = self._get_scene_description(scene)
        choices = self._get_available_choices(scene)
        inventory = self.player.inventory
        
        # Combine game message with scene description
        full_description = f"{self.message}\n\n{description}" if self.message else description
        self.message = "" # Clear message after retrieving it

        return {
            "description": full_description.strip(),
            "choices": choices,
            "inventory": inventory,
            "is_game_over": not choices
        }

    def _get_scene_description(self, scene):
        """Gets the description, generating it via AI if required."""
        if scene.get('is_ai_generated') and self.ai_engine:
            prompt = scene.get('prompt', "Describe this scene.")
            return self.ai_engine.generate_text(prompt)
        return scene.get('description', "You've reached an uncharted area.")

    def _get_available_choices(self, scene):
        """Returns choices, checking for item requirements."""
        item_needed = scene.get('item_needed')
        if item_needed and not self.player.has_item(item_needed):
            # Show a failure description and a single choice to go back or acknowledge
            return {"Continue": self.current_scene_id}
        return scene.get('choices', {})

    def process_input(self, choice_text):
        """Processes the player's choice and updates the game state."""
        scene = self.story.get(self.current_scene_id)
        
        # Handle cases where an item was needed but not present
        item_needed = scene.get('item_needed')
        if item_needed and not self.player.has_item(item_needed):
            self.message = scene.get('fail_description', f"You need a {item_needed} to proceed.")
            # Don't change the scene, just show the message
            return

        if choice_text in scene['choices']:
            next_scene_id = scene['choices'][choice_text]
            self.current_scene_id = next_scene_id
            
            # Check for new items in the new scene
            new_scene = self.story.get(self.current_scene_id, {})
            item_given = new_scene.get('item_given')
            if item_given:
                self.message = self.player.add_item(item_given)