import box
import prisoner

number_of_prisoners = 100
attempts_per_prisoner = 50
test_attempts = 1000
successful_escapes = 0

if __name__ == '__main__':
    # Setup random boxes
    print('Number of prisoners: %d' % number_of_prisoners)

    for i in range(test_attempts):
        prisoner_boxes = box.build_boxes(number_of_prisoners)

        # Create prisoners
        prisoners = prisoner.gather_prisoners(number_of_prisoners)

        # Have prisoners search
        for p in prisoners:
            p.search_boxes(prisoner_boxes, attempts_per_prisoner)

        # Calculate success
        if len([p for p in prisoners if p.found_number]) == number_of_prisoners:
            successful_escapes += 1

    print('Escape Success Rate: %.0f%% of %d attempts' % (100 * (successful_escapes / test_attempts), test_attempts))

