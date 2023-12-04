def map_int_list(list):
    return set([int(i) for i in list])


def get_two_list(card):
    left_list, right_list = card.split("|")
    left_list = left_list.split(":")[1]
    left_list, right_list = left_list.split(), right_list.split()
    return map_int_list(left_list), map_int_list(right_list)


def part_one(input_data, part = 1):
    total_points = 0
    for_part_two = []
    for card in input_data:
        winning_list, my_list = get_two_list(card)
        my_winning_numbers = 0
        for number in winning_list:
            if number in my_list:
                my_winning_numbers += 1
        total_points += int(2 ** (my_winning_numbers - 1))
        for_part_two.append(int(my_winning_numbers))
    if part == 2:
        return for_part_two
    return total_points


def part_two(input_data):
    total_cards = len(input_data)
    total_points = part_one(input_data, 2)
    cards_count = {}
    for card_number in range(total_cards):
        cards_count[card_number] = 1
    for card_number in range(total_cards):
        for add_card_point in range(card_number + 1, card_number + total_points[card_number] + 1):
            if add_card_point >= total_cards:
                break
            cards_count[add_card_point] += cards_count[card_number]
    total_scratchcards = 0
    for card_number in range(total_cards):
        total_scratchcards += cards_count[card_number]
    return total_scratchcards


input_data = open('input.txt', 'r').read().split('\n')

# Part 1
print(part_one(input_data, 1))

# Part 2
print(part_two(input_data))
