def displayScene(scene):
        print(scene["description"])
        print("\nChoices")
        # Display choices
        
        
        for i, choice in enumerate(scene["choices"], 1):
            print(f"{i}. {choice['text']}")
        print()
        
def getChoice(scene):
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                # Validate choice
                if 1 <= choice <= len(scene["choices"]):
                    return scene["choices"][choice - 1]["next_scene"]
                else:
                    print("Invalid choice. Please try again.")
            # Handle non-integer input
            except ValueError:
                print("Please enter a valid number.")
        
# Function to display the current scene and its choices
def playGame():
    scenes = {
        "start": {
            "description": """The Jungle of Mystara looms before you, its canopy a tangle of emerald vines and vibrant flowers. The air hums with the buzz of insects and distant animal calls. Legends say the Crystal of Eternity lies deep within. A narrow trail snakes into the jungle’s heart, while to the west, the roar of rushing water beckons. A tall tree nearby offers a vantage point, if you dare to climb.""",
            "choices": [
                {"text": "Follow the narrow trail into the jungle", "next_scene": "clearing"},
                {"text": "Head toward the sound of rushing water", "next_scene": "river"},
                {"text": "Climb the tree for a better view", "next_scene": "tree"}
            ]
        },
        "clearing": {
            "description": """The trail opens into a sunlit clearing, where ancient stone ruins rise from the earth, their surfaces choked with vines. Two paths diverge: one descends into a shadowy cave, its entrance yawning like a hungry maw; the other leads to a rickety rope bridge swaying over a misty chasm. The ruins themselves seem to whisper secrets, inviting closer inspection.""",
            "choices": [
                {"text": "Enter the shadowy cave", "next_scene": "cave"},
                {"text": "Cross the rickety rope bridge", "next_scene": "bridge"},
                {"text": "Examine the ancient ruins", "next_scene": "ruins"}
            ]
        },
        "river": {
            "description": """You reach the banks of a raging river, its waters churning over jagged rocks. Across the torrent, a faint glimmer catches your eye—could it be the Crystal? The current looks dangerous, but a safer crossing might lie upstream. The jungle path behind you offers a way back to safety.""",
            "choices": [
                {"text": "Attempt to cross the river", "next_scene": "game_over_drown"},
                {"text": "Search upstream for a safer crossing", "next_scene": "bridge"},
                {"text": "Return to the jungle path", "next_scene": "start"}
            ]
        },
        "tree": {
            "description": """You scale a towering tree, its bark rough under your hands. From a high branch, you glimpse a golden-roofed temple in the distance, its spires piercing the canopy. Suddenly, a branch cracks beneath you, leaving you clinging precariously. Climbing higher might reveal more, but the temple calls, and descending safely is an option.""",
            "choices": [
                {"text": "Climb higher for a better view", "next_scene": "game_over_fall"},
                {"text": "Descend carefully to the ground", "next_scene": "temple"},
                {"text": "Leap to the temple’s roof", "next_scene": "game_over_fall"}
            ]
        },
        "cave": {
            "description": """The cave is a labyrinth of damp stone, its darkness swallowing the light. A low growl echoes from deeper within, sending a chill down your spine. You could press forward, hoping to find a way through, or retreat to the safety of the clearing.""",
            "choices": [
                {"text": "Proceed deeper into the cave", "next_scene": "game_over_beast"},
                {"text": "Turn back to the clearing", "next_scene": "clearing"}
            ]
        },
        "bridge": {
            "description": """A rickety rope bridge sways over a yawning chasm, its boards creaking ominously. Far below, jagged rocks gleam in the mist. Crossing is risky, but the path beyond might lead to the Crystal. The clearing behind you is a tempting retreat.""",
            "choices": [
                {"text": "Attempt to cross the bridge", "next_scene": "game_over_fall"},
                {"text": "Return to the clearing", "next_scene": "clearing"}
            ]
        },
        "ruins": {
            "description": """The ruins pulse with ancient energy, their carvings depicting forgotten rituals. A faint path winds toward a temple in the distance, its golden spire visible through the trees. The clearing remains an option if you wish to explore elsewhere.""",
            "choices": [
                {"text": "Follow the path to the temple", "next_scene": "temple"},
                {"text": "Return to the clearing", "next_scene": "clearing"}
            ]
        },
        "temple": {
            "description": """You step into a grand temple, its walls aglow with shimmering runes that pulse like heartbeats. At the chamber’s heart, the Crystal of Eternity rests on a pedestal, radiating soft light. But the runes seem to warn of danger. Do you seize the prize or heed the ancient carvings?""",
            "choices": [
                {"text": "Take the Crystal of Eternity", "next_scene": "win"},
                {"text": "Examine the runes first", "next_scene": "game_over_trap"}
            ]
        },
        "win": {
            "description": """As you grasp the Crystal, the runes flare to life, and a wave of energy surges through you. The jungle trembles, but you emerge unscathed, the Crystal in hand. You have found the legendary Crystal of Eternity! You win!""",
            "choices": []
        },
        "game_over_drown": {
            "description": """You plunge into the river’s icy waters, but the current is relentless. It sweeps you over rocks and into the depths. The Jungle of Mystara claims another soul. Game Over.""",
            "choices": []
        },
        "game_over_fall": {
            "description": """Your footing fails, and you plummet into the chasm below. The jungle’s canopy closes above you as darkness takes hold. Game Over.""",
            "choices": []
        },
        "game_over_beast": {
            "description": """In the cave’s pitch-black depths, a massive jaguar leaps from the shadows, its eyes glinting with hunger. Without a way to fend it off, the jungle claims its prize. Game Over.""",
            "choices": []
        },
        "game_over_trap": {
            "description": """As you study the runes, a low rumble shakes the temple. The floor gives way, and ancient traps spring to life, collapsing the chamber around you. The Crystal remains out of reach. Game Over.""",
            "choices": []
        }
    }   
    #Introductory of the Adventure Game: Jungle of Mystara
    print("Welcome Lost Explorer to the Jungle of Mystara\n")
    print("You are an intrepid explorer venturing into the uncharted Jungle of Mystara")
    print("Your journey is fraught with danger—wild beasts, treacherous terrain, and ancient traps guard the prize.")
    print("Every decision shapes your fate: will you find the Crystal, or be lost forever in the jungle’s embrace?\n")
    input("To begin your adventure, press Enter...\n")

    currentScene = "start"
    while True:
        # Display the current scene and choices
        displayScene(scenes[currentScene])
        if not scenes[currentScene]["choices"]:
            print("\nGame Ended. Thanks for playing!")
            break

        currentScene = getChoice(scenes[currentScene])
    #start the game
if __name__ == "__main__":
    playGame()