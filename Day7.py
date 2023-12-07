from collections import Counter


def get_point(card_map):
    c_map = sorted(card_map.values(), reverse = True)
    if c_map == [5]:
        return 7
    if c_map == [4, 1]:
        return 6
    if c_map == [3, 2]:
        return 5
    if c_map == [3, 1, 1]:
        return 4
    if c_map == [2, 2, 1]:
        return 3
    if c_map == [2, 1, 1, 1]:
        return 2
    return 1


def find_ind_strength(str, part):
    processed_str = []
    processed_str_map = {}
    for s in str:
        ss = []
        for ch in s:
            ss.append(map_card(ch, part))
        processed_str_map[tuple(ss)] = s
        processed_str.append(ss)
    processed_str.sort()
    ind_points_map = {}
    rank = 1
    for s in processed_str:
        ind_points_map[processed_str_map[tuple(s)]] = rank
        rank += 1
    ind_points = []
    for s in str:
        ind_points.append(ind_points_map[s])
    return ind_points


def map_card(ch, part = 1):
    if ch == 'A':
        return 14
    elif ch == 'K':
        return 13
    elif ch == 'Q':
        return 12
    elif ch == 'J':
        if part == 2:
            return 1
        return 11
    elif ch == 'T':
        return 10
    else:
        return int(ch)


def process_data(input_data, processed_data = [], part = 1):
    if part == 1:
        processed_data = input_data[::]
    points = []
    ind_strength = find_ind_strength([line.split()[0] for line in input_data], part)
    for org_line, line, ind_point in zip(input_data, processed_data, ind_strength):
        card, bid = line.split()
        org_card, org_bid = org_line.split()
        card_map = {}
        for c in card:
            if c not in card_map:
                card_map[c] = 0
            card_map[c] += 1
        points.append([get_point(card_map), ind_point, org_card, org_bid])
    points.sort(key = lambda x: (-x[0], -x[1]))
    rank_map = {}
    rank = len(input_data)
    for s in points:
        rank_map[s[2]] = rank
        rank -= 1
    ans = 0
    for line in input_data:
        card, bid = line.split()
        ans += (int(bid) * rank_map[card])
    return ans


def process_data_for_part2(input_data):
    processed_data_for_part2 = []
    for line in input_data:
        card_processed = ""
        card, bid = line.split()
        card_dist = Counter()
        for ch in card:
            if ch != 'J':
                card_dist[ch] += 1
        if not card_dist.most_common():
            most_occured_card = 'A'
        else:
            max_occured_count = card_dist.most_common()[0][1]
            most_occured_card = card_dist.most_common()[0][0]
            for char, count in card_dist.most_common():
                if count == max_occured_count:
                    if map_card(most_occured_card) < map_card(char):
                        most_occured_card = char
                else:
                    break
        for ch in card:
            if ch == 'J':
                card_processed += most_occured_card
            else:
                card_processed += ch
        processed_data_for_part2.append(card_processed + ' ' + bid)
    return processed_data_for_part2


input_data = open('input.txt', 'r').read().split('\n')

# Part 1
print(process_data(input_data))

# Part 2
processed_data = process_data_for_part2(input_data)
print(process_data(input_data, processed_data, 2))
