import string

def solve(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        p1, p2 = line[:len(line)//2], line[len(line)//2:]
        a = list(set(p1) & set(p2))[0]
        if (a.islower()):
            sum += list(string.ascii_lowercase).index(a) + 1
        elif (a.isupper()):
            sum += list(string.ascii_uppercase).index(a) + 27
    return sum


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.readlines()))
