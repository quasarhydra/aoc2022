
def solve(lines):
    trees = []
    for line in lines:
        line = line.strip()
        trees.append([eval(x) for x in list(line)])
    count = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            col = [row[j] for x, row in enumerate(trees)]
            row = [col for x, col in enumerate(trees[i])]
            if ((max(col[0:i]) < trees[i][j]) or (max(col[i+1:]) < trees[i][j]) or (max(row[0:j]) < trees[i][j]) or (max(row[j+1:]) < trees[i][j])):
                count += 1

    count += (len(trees) + len(trees[0])) * 2 - 4

    return count


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.readlines()))
