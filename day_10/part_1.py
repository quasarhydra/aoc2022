
from itertools import cycle


def solve(lines):
    x = [1]
    for line in lines:
        line = line.strip()
        if line == 'noop':
            x.append(x[-1])

        elif line.startswith('addx'):
            op, value = line.split(' ')
            x += ([x[-1], x[-1] + int(value)])
    return (sum([x[19]*20, x[59]*60, x[99]*100, x[139]*140, x[179]*180, x[219]*220]))


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.readlines()))
