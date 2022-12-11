

def solve(lines):
    x = [1]
    crt = [['.'] * 40 for i in range(6)]

    for line in lines:
        line = line.strip()
        if line == 'noop':
            x.append(x[-1])

        elif line.startswith('addx'):
            op, value = line.split(' ')
            x += ([x[-1], x[-1] + int(value)])

    for i in range(0, 6):
        for j in range(40):
            if (x[j + (i*40)] == j):
                crt[i][j] = '#'
                print('q')
            if (x[j + (i*40)] - 1 == j):
                crt[i][j] = '#'
                print('w')
            if (x[j + (i*40)] + 1 == j):
                print('e')
                crt[i][j] = '#'

    print(*crt, sep='\n')


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.readlines()))
