
def solve(lines):
    for i in range(0, len(lines)):
        if (len(set(lines[i:i+14])) == 14):
            print(lines[i:i+14])
            return i+14


with open("input.txt", encoding='utf-8') as f:
    print(solve(f.read()))
