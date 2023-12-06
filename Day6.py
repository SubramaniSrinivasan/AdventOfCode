def find(time, dis):
    win_ans = 1
    for t, d in zip(time, dis):
        win_count = 0
        for hold in range(t):
            dis_travelled = (t - hold) * hold
            if dis_travelled > d:
                win_count += 1
        win_ans *= win_count
    return win_ans


def process_input_for_part_one(input_data):
    time = [int(t.strip()) for t in input_data[0].split(':')[1].split()]
    dis = [int(t.strip()) for t in input_data[1].strip().split(':')[1].split()]
    return time, dis


def process_input_for_part_two(input_data):
    time = [int(''.join([t.strip() for t in input_data[0].split(':')[1].split()]))]
    dis = [int(''.join([t.strip() for t in input_data[1].strip().split(':')[1].split()]))]
    return time, dis


input_data = open('input.txt', 'r').read().split('\n')

# Part 1
time, dis = process_input_for_part_one(input_data)
print(find(time, dis))

#Part 2
time, dis = process_input_for_part_two(input_data)
print(find(time, dis))
