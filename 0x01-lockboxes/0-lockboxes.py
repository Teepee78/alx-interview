#!/usr/bin/python3
"""
Defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked

    Args:
        boxes (list): list of boxes to check

    Returns:
        bool: True if all boxes can be unlocked, False otherwise
    """
    i = len(boxes)

    # Create map
    map = {}
    for i, box in enumerate(boxes):
        if i == 0:
            map[i] = {
                "open": True,
                "items": box
            }
        else:
            map[i] = {
                "open": False,
                "items": box
            }

    # Iterate map and open boxes
    while i > 0:
        for box in map.values():
            if box['open']:
                # Open all boxes that box holds key for
                for item in box['items']:
                    if item < len(boxes) and item >= 0:
                        map[item]['open'] = True
        i -= 1

    # Check if all boxes were opened
    for box in map.values():
        if not box['open']:
            return False
    return True
