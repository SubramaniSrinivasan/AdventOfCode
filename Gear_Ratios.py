def isdigit(x):
    return '0' <= x <= '9'
def check_one(i, j):
    for t1 in range(-1, 2):
        for t2 in range(-1, 2):
            if 0 <= i + t1 < r and 0 <= j + t2 < c and not isdigit(a[i + t1][j + t2]) and a[i + t1][j + t2] != '.':
                return True
    return False

def check_two(i, j):
    for t1 in range(-1, 2):
        for t2 in range(-1, 2):
            if 0 <= i + t1 < r and 0 <= j + t2 < c and not isdigit(a[i + t1][j + t2]) and a[i + t1][j + t2] != '.':
                if a[i + t1][j + t2] == '*':
                    if (i + t1, j + t2) not in d:
                        d[(i + t1, j + t2)] = []
                    d[(i + t1, j + t2)].append((i, j))
                return True
    return False

def part_1():
    ans = 0
    for i in range(r):
        t = 0
        ct = False
        for j in range(c):
            if isdigit(a[i][j]):
                t = (10 * t) + int(a[i][j])
                ct |= check_one(i, j)
            else:
                if ct:
                    ans += t
                t = 0
                ct = False
            if j == c - 1:
                if ct:
                    ans += t
    return ans

def part_2():
    ans = 0

    for i in range(r):
        t = 0
        ct = False
        for j in range(c):
            if isdigit(a[i][j]):
                t = (10 * t) + int(a[i][j])
                ct |= check_two(i, j)
            else:
                if ct:
                    ans += t
                t = 0
                ct = False
            if j == c - 1:
                if ct:
                    ans += t
    ans = 0

    for i, j in d:
        dd = {}
        for k, j in d[(i, j)]:
            t1, t2 = j, j + 1
            ct = []
            t = ""
            while t1 >= 0 and isdigit(a[k][t1]):
                t = a[k][t1] + t
                ct.append((k, t1))
                t1 -= 1
            while t2 < c and isdigit(a[k][t2]):
                t += a[k][t2]
                ct.append((k, t2))
                t2 += 1
            ct.sort()
            dd[tuple(ct)] = int(t)
        if len(dd) == 2:
            res = 1
            for k in dd:
                res *= dd[k]
            ans += res
    return ans

a = open('input.txt', 'r').read().split('\n')
r, c = len(a), len(a[0])
d = {}

# Part 1
print(part_1())

# Part 2
print(part_2())