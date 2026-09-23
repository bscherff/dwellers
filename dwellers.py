"""
Cave Adventure - A simple text-based adventure game
A proof-of-concept for branching story games in Python.

Run with: python3 dwellers.py
"""

# Each "room" is a dictionary with a description and choices.
# Each choice maps player input -> the key of the next room.
rooms = {
    "start": {
        "description": (
            "You stand at the mouth of a dark cave. Cold air drifts out.\n"
            "There's a torch mounted on the wall beside you, still burning.\n"
            "In the distance, you hear a low growl."
        ),
        "choices": {
            "take torch": "torch_room",
            "enter cave": "dark_room",
            "run away": "coward_ending",
        },
    },
    "torch_room": {
        "description": (
            "You grab the torch. The flame flickers, casting long shadows.\n"
            "Ahead, the cave splits into two tunnels: one heads left, one heads right."
        ),
        "choices": {
            "go left": "left_tunnel",
            "go right": "right_tunnel",
        },
    },
    "dark_room": {
        "description": (
            "You step into the dark cave without a light.\n"
            "You trip over a rock almost immediately. This was a bad idea."
        ),
        "choices": {},
        "ending": "You stumble in the dark and twist your ankle. GAME OVER.",
    },
    "left_tunnel": {
        "description": (
            "The left tunnel opens into a small chamber.\n"
            "A sleeping bear lies in the corner, and beside it glints a pile of gold."
        ),
        "choices": {
            "take gold": "bear_ending",
            "back away quietly": "right_tunnel",
        },
    },
    "right_tunnel": {
        "description": (
            "The right tunnel leads to an underground spring.\n"
            "The water is clear, and you can see something shiny at the bottom."
        ),
        "choices": {
            "dive in": "dive_in_water",
            "leave it alone": "safe_ending",
        },
    },
    "dive_in_water": {
        "description": (
            "With a quiet splash, you dive head-first into the water, which cools your skin.\n"
            "You see the shiny object more clearly, however, it remains out of reach."
        ),
        "choices": {
            "keep swimming": "keep_swimming",
            "resurface for another breath": "resurface",
        },
    },
    "keep_swimming": {
        "description": (
            "You reach the base of the spring, and with water gently pushing you back towards the surface, you see what looks like a silver pendant necklace.\n"
            "Heart pounding from the lack of oxygen and the potential discovery, you realize you need to act quickly."
        ),
        "choices": {
            "grab the necklace by the chain": "necklace",
            "kick off the floor and swim for the surface": "resurface",
        },
    },
    "resurface": {
        "description": (
            "You break the smooth surface of the water, first with your arms, then your head, and take a breath while treading water.\n"
            "The movement of the water sends reflected light and shadows bouncing off of the cave walls. You think you see movement down the tunnel."
        ),
        "choices": {
            "keep swimming": "keep_swimming",
            "get out and go back to where the tunnels split": "tunnel_split_movement"
        },
    },
    "necklace": {
        "description": (
            "Your right hand drags through the water and feels the seemingly delicate silver chain, gently pulls upwards, and frees the heavy pendant from the bottom of the spring.\n"
            "You notice a stream of air bubbles starts rising from the source of the spring, slowly at first, then faster and faster until the force is pushing you back to the surface."
            ),
        "choices": {
            "swim with the necklace in your hand": "necklace_in_hand_ending",
            "place the chain around your neck": "necklace_on_neck_ending"
        },
    },
    "tunnel_split_movement": {
        "description": (
            "You feel as if someone, or something, has just moved through the hall. No visible sign, but a sense of movement, an inaudible rustling, an imperceptible breeze, subconsciously prevents you from remaining relaxed.\n"
            "Alone, wet, cold, and now on edge, you shiver slightly.\n"
            "\n"
            "The torch burns lower.\n"
            "\n"
            "Absorbed in the flame, you lose yourself for a moment."
            "\n"
            "The noise becomes perceptible. Another low growl emminates from the other tunnel."
        ),
        "choices": {
            "sit down to dry off": "sit_down_ending",
            "explore the left tunnel and the noise" : "left_tunnel"
        },
    },
    "necklace_on_neck_ending": {
        "description": "",
        "choices": {},
        "ending": "The necklace suddenly grows heavier and heavier, dragging you back to the bottom and closing around your neck. You drown. GAME OVER.",
    },
    "necklace_in_hand_ending": {
            "description": "",
        "choices": {},
        "ending": ( "The necklace suddenly grows heavier and heavier, dragging you back to the bottom, and you release it, striving with all your might for the surface.\n"
        "You make your way to the edge of the water, climb onto the damp floor of the cave, gasping for breath.\n"
        "Realizing how lucky you are, you regain your composure, say a prayer of thanks, and return home, realizing watery treasure hunts are not worth your life.\n"
        "As you grow old, surrounded by your family, you remember the day you stopped chasing after vainglory and playing text-adventure video games, content and at peace. THE END."
        ),
    },
    "coward_ending": {
        "description": "",
        "choices": {},
        "ending": "You run home. Safe, but you'll always wonder what was in that cave.",
    },
    "bear_ending": {
        "description": "",
        "choices": {},
        "ending": "The bear wakes up. It is NOT happy. GAME OVER.",
    },
    "treasure_ending": {
        "description": "",
        "choices": {},
        "ending": "You find an ancient coin at the bottom of the spring. You win!",
    },
    "safe_ending": {
        "description": "",
        "choices": {},
        "ending": "You leave the spring undisturbed and head home with a good story. THE END.",
    },
    "sit_down_ending": {
        "description": "",
        "choices": {},
        "ending": ("You sit down, and start to warm yourself, but the torch won't cut through the chilly and damp cave air.\n"
        "You fall asleep.\n"
        "\n"
        "\n"
        "\n"
        "The bear wakes you up. You scream. GAME OVER."),
    },
}

def play():
    current = "start"

    while True:
        room = rooms[current]

        print("\n" + room["description"])

        # If there are no choices, this room is an ending.
        if not room["choices"]:
            print("\n" + room["ending"] + "\n")
            break

        # Show the available choices.
        options = list(room["choices"].keys())
        print("\nWhat do you do?")
        for option in options:
            print(f"  - {option}")

        # Get player input, matched case-insensitively.
        player_input = input("\n> ").strip().lower()

        if player_input in room["choices"]:
            current = room["choices"][player_input]
        else:
            print("\nYou're not sure how to do that. Try again.")


if __name__ == "__main__":
    print("=" * 50)
    print("        THE CAVE")
    print("=" * 50)
    play()
