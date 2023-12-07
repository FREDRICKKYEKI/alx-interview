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
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_index = unseen_boxes.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_index])
            seen_boxes.add(box_index)
    return n == len(seen_boxes)
