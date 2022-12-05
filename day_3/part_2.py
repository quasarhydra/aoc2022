import string


def solve(lines):
    def split():
        for i in range(0, len(lines), 3):
            yield lines[i:i + 3]
    groups = list(split())
    sum = 0
    for group in groups:
        a = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        if (a.islower()):
            sum += list(string.ascii_lowercase).index(a) + 1
        elif (a.isupper()):
            sum += list(string.ascii_uppercase).index(a) + 27
    return sum


with open("input.txt", encoding='utf-8') as f:
    print(solve([s.strip() for s in f.readlines()]))
