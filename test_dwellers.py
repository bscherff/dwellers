"""Structural tests for the rooms dict in dwellers.py.

These don't play the game — they just check the data is internally
consistent, catching the kind of bug that causes a crash mid-game
(e.g. a choice pointing at a room key that doesn't exist).
"""

from dwellers import rooms


def test_start_room_exists():
    assert "start" in rooms


def test_every_room_has_a_description():
    for key, room in rooms.items():
        assert isinstance(room["description"], str), f"{key} description is not a string"


def test_every_choice_points_to_a_real_room():
    for key, room in rooms.items():
        for choice_text, target in room["choices"].items():
            assert target in rooms, (
                f"room '{key}' choice '{choice_text}' points to missing room '{target}'"
            )


def test_rooms_without_choices_have_an_ending():
    for key, room in rooms.items():
        if not room["choices"]:
            assert "ending" in room, f"room '{key}' has no choices and no ending"
            assert isinstance(room["ending"], str)


def test_rooms_with_an_ending_have_no_choices():
    for key, room in rooms.items():
        if "ending" in room:
            assert not room["choices"], f"room '{key}' has both an ending and choices"
