
def solve(lines):
    trees = []
    for line in lines:
        line = line.strip()
        trees.append([eval(x) for x in list(line)])
    views = []
    for i in range(0, len(trees)):
        for j in range(0, len(trees[0])):
            col = [row[j] for x, row in enumerate(trees)]
            row = [col for x, col in enumerate(trees[i])]
            view = 1
            for _, v in enumerate(col[0:i][::-1]):
                if v >= trees[i][j]:
                    view *= (_ + 1)
                    break
                if (_ == len(col[0:i][::-1]) - 1):
                    view *= len(col[0:i][::-1])

            for _, v in enumerate(col[i+1:]):
                if v >= trees[i][j]:
                    view *= (_ + 1)
                    break
                if (_ == len(col[i+1:]) - 1):
                    view *= len(col[i+1:])

            for _, v in enumerate(row[0:j][::-1]):
                if v >= trees[i][j]:
                    view *= (_ + 1)
                    break
                if (_ == len(row[0:j][::-1]) - 1):
                    view *= len(row[0:j][::-1])

            for _, v in enumerate(row[j+1:]):
                if v >= trees[i][j]:
                    view *= (_ + 1)
                    break
                if (_ == len(row[j+1:]) - 1):
                    view *= len(row[j+1:])

            views.append(view)

    return views


with open("input.txt", encoding='utf-8') as f:
    print(max(solve(f.readlines())))
