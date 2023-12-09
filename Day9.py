def check_non_zero(li):
    for i in li:
        if i != 0:
            return True
    return False


def process(input_data, part = 1):
    res = 0
    for line in input_data:
        input_list = [int(i) for i in line.split()]
        processed_list = []
        curr_list = input_list[:]
        processed_list.append(input_list[:])
        curr_list_len = len(input_list)
        while curr_list_len > 1:
            next_list = []
            for i in range(1, curr_list_len):
                next_list.append(curr_list[i] - curr_list[i - 1])
            processed_list.append(next_list)
            curr_list = next_list[:]
            curr_list_len -= 1
            if not check_non_zero(curr_list):
                break
        ans = 0
        for i in processed_list[::-1]:
            if part == 1:
                ans = i[-1] + ans
            else:
                ans = i[0] - ans
        res += ans
    return res


input_data = open('input.txt', 'r').read().split('\n')

# Part 1
part = 1
ans1 = process(input_data, part)
print(ans1)

#Part 2
part = 2
ans2 = process(input_data, part)
print(ans2)
