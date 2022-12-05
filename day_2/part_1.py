
with open("input.txt", encoding='utf-8') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        move = line.strip().split(" ")
        if ((move[0] == 'A' and move[1] == 'X') or (move[0] == 'B' and move[1] == 'Y') or (move[0] == 'C' and move[1] == 'Z')):
            sum += 3
        elif ((move[1] == 'X' and move[0] == 'C') or (move[1] == 'Y' and move[0] == 'A') or (move[1] == 'Z' and move[0] == 'B')):
            sum += 6

        if move[1] == 'X':
            sum += 1
        elif move[1] == 'Y':
            sum += 2
        else:
            sum += 3
    print(sum)
