import random


class PrisonerBox:
    index: int
    prisoner_id: int

    def __init__(self, index, prisoner_id):
        self.index = index
        self.prisoner_id = prisoner_id


def build_boxes(box_count: int) -> []:
    prisoner_ids = []
    boxes = []
    for i in range(0, box_count):
        prisoner_ids.append(i)

    i = 0
    while len(prisoner_ids) > 0:
        prisoner_id = random.randint(0, len(prisoner_ids) - 1)
        boxes.append(PrisonerBox(i, prisoner_ids[prisoner_id]))
        prisoner_ids.pop(prisoner_id)
        i += 1

    return boxes
