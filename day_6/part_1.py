
def solve(lines):
    for i in range(0, len(lines)):
        if (len(set(lines[i:i+4])) == 4):
            print(lines[i:i+4])
            return i+4


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.read()))
