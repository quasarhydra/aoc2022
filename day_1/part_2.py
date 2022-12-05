

with open("input.txt", encoding='utf-8') as f:
    lines = f.readlines()
    numbers = []
    i = 0
    for line in lines:
        if line.strip():
            i += int(line)
        else:
            numbers.append(i)
            i = 0
    numbers.append(i)
    numbers.sort(reverse=True)
    print(sum(numbers[:3]))
