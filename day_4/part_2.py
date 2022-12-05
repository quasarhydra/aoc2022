

def solve(lines):
    for line in lines:
        e1 = [int(i) for i in line.split(',')[0].split('-')]
        e2 = [int(i) for i in line.split(',')[1].split('-')]
        yield ((e1[0] >= e2[0] and e1[0] <= e2[1]) or (e1[1] <= e2[1] and e1[1] >= e2[0]) or ((e1[0] <= e2[0] and e1[1] >= e2[0]) or (e1[1] >= e2[1] and e1[0] <= e2[1])))


with open("input.txt", encoding='utf-8') as f:
    print(sum(list(solve([s.strip() for s in f.readlines()]))))
