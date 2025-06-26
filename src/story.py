# src/story.py

STORY_DATA = {
    'START': {
        'description': "You awaken at the edge of a dark, ancient forest. A cold mist clings to the ground. To your left, a narrow path winds into the woods. To your right, a weathered signpost stands crookedly.",
        'choices': {
            "Take the narrow path into the forest.": "FOREST_PATH",
            "Examine the weathered signpost.": "SIGNPOST"
        }
    },
    'SIGNPOST': {
        'description': "The sign is covered in moss. You scrape it away to read the faint carving: 'BEWARE THE WHISPERING CAVES'. A small, rusty key is wedged into a crack in the wood.",
        'item_given': "rusty key",
        'choices': {
            "Take the key and head down the forest path.": "FOREST_PATH",
            "Ignore the key and go back to the edge of the forest.": "START"
        }
    },
    'FOREST_PATH': {
        'description': "The path is overgrown and shadows dance between the trees. After a few minutes, you arrive at a cliff face. A dark cave entrance gapes before you, sealed by an old wooden door with a rusty lock.",
        'item_needed': "rusty key",
        'choices': {
            "Use the rusty key to unlock the door.": "CAVE_ENTRANCE",
            "Search the area for another way in.": "SEARCH_AREA"
        },
        'fail_description': "The door is locked tight. You need a key to open it. You should look for one."
    },
    'CAVE_ENTRANCE': {
        'description': "The key turns with a loud *click*. The door creaks open, revealing a dark tunnel. A cool, damp air flows out, carrying the scent of earth and something... else. You step inside.",
        'choices': {
            "Venture deeper into the darkness.": "DARK_TUNNEL",
        }
    },
    'SEARCH_AREA': {
        'description': "You spend time searching the cliff face but find no other entrance. The only way forward seems to be through the locked door.",
        'choices': {
            "Return to the locked door.": "FOREST_PATH"
        }
    },
    'DARK_TUNNEL': {
        'is_ai_generated': True,
        'prompt': "You are in a dark, mysterious cave tunnel. Describe the strange, glowing mushrooms on the walls and the sound of distant dripping water, creating a sense of wonder and suspense.",
        'choices': {
            "Follow the sound of dripping water.": "WATER_SOUND",
            "Examine the glowing mushrooms.": "MUSHROOMS"
        }
    },
    'WATER_SOUND': {
        'description': "You follow the echoing drips to a vast underground chamber. In the center, a shimmering pool of water glows with an ethereal light. A small, silver locket rests on a pedestal by the water's edge.",
        'item_given': "silver locket",
        'choices': {
            "Take the locket and return to the main tunnel.": "DARK_TUNNEL",
            "Drink from the shimmering pool.": "GAME_OVER_WATER"
        }
    },
    'MUSHROOMS': {
        'description': "The mushrooms pulse with a soft, blue light. As you touch one, a cloud of spores erupts. You feel dizzy for a moment, but then a strange clarity fills your mind. You feel more perceptive.",
        'choices': {
            "Continue down the tunnel.": "WATER_SOUND"
        }
    },
    'GAME_OVER_WATER': {
        'description': "The water is invigorating but intensely magical. Your body dissolves into pure light, becoming one with the cave's energy forever. Your adventure ends here.",
        'choices': {}
    },
    'END': {
        'description': "This is a placeholder ending. Congratulations!",
        'choices': {}
    }
}