
def solve(lines):
    in1, in2 = lines.split('\n\n')
    line = in1.split('\n')
    rows = [x.split(' ') for x in line]
    crates = [[] for _ in list(filter(None, rows.pop()))]
    rows = rows[::-1]
    for i, row in enumerate(rows):
        j = 0
        while j < len(row):
            if (row[j]):
                crates[i].append(row[j].strip('[]'))
            elif ((len(set(row[j-3:j])) == 1) and row[j] == ''):
                crates[i].append('')
                if j+1 < len(row) and row[j+1] == '':
                    j += 3

            j += 1

    crates = [x for x in crates if x]
    crates = list(map(list, zip(*crates)))
    crates = [list(filter(None, x)) for x in crates]
    moves = [[int(s) for s in x.split() if s.isdigit()]
             for x in in2.split('\n')]
    for move in moves:
        items = crates[move[1] - 1][-move[0]:]
        crates[move[1] - 1] = crates[move[1] - 1][:-move[0]]
        crates[move[2] - 1] = crates[move[2] - 1] + items
    for crate in crates:
        yield crate.pop()


with open("input.txt", encoding='utf-8') as f:
    print(''.join(list(solve(f.read()))))
