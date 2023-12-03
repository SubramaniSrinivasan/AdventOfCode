def process(s):
    n = len(s)
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    t = ""
    i = 0
    while i < n:
        f = False
        for j in numbers:
            if s[i:i+len(j)] == j:
                t += str(numbers.index(j) + 1)
                i += 1
                f = True
                break
        if not f:
            t += s[i]
            i += 1
    return t

def find(data, part = 1):
    ans = 0
    for line in data:
        if part == 2:
            line = process(line)
        res = [int(i) for i in line if i.isdigit()]
        ans += ((res[0] * 10) + res[-1])
    return ans

data = open('input.txt', 'r').read().split('\n')
# Part 1
print(find(data))

# Part 2
print(find(data, 2))