#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the
other boxes.
Write a method that determines if all the boxes can be opened.
    - Prototype: def canUnlockAll(boxes)
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    if boxes is None or len(boxes) == 0:
        return False

    keys = [0]
    for key in keys:
        print(keys)
        for newKey in boxes[key]:
            if newKey not in keys and newKey < len(boxes):
                keys.append(newKey)
    if len(keys) == len(boxes):
        return True
    return False
