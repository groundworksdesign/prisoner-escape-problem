import box


class Prisoner:
    number: int
    found_number: bool
    attempt_count: int

    def __init__(self, number):
        self.number = number
        self.found_number = False
        self.attempt_count = 0

    def search_boxes(self, prison_boxes: [], attempts_per_prisoner: int):
        self.attempt_count += 1
        box_number = prison_boxes[self.number].prisoner_id
        if box_number == self.number:
            self.found_number = True
        else:
            while self.attempt_count < attempts_per_prisoner:
                self.attempt_count += 1
                search_box = box_number
                box_number = prison_boxes[search_box].prisoner_id
                if box_number == self.number:
                    self.found_number = True
                    break


def gather_prisoners(numer_of_prisoners: int) -> []:
    prisoners = []
    for i in range(0, numer_of_prisoners):
        prisoners.append(Prisoner(i))
    return prisoners

    



