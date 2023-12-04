#!/usr/bin/python3
''' A module for working with lockboxes '''


def canUnlockAll(boxes):
    '''
        Determines if all the boxes can be opened or not
        Returns:
            True: all boxes can be opened
            False: not all boxes can be opened
    '''
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        boxIdx = locked_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[boxIdx])
            unlocked_boxes.add(boxIdx)
    return n == len(unlocked_boxes)