
def play(p):
    if p == 'A' or p == 'D':
        return 1
    elif p == 'B':
        return 2
    elif p == 'C' or p =='@': 
        return 3

with open("input.txt", encoding='utf-8') as f:
   lines = f.readlines()
   sum = 0
   for line in lines:
       move = line.strip().split(" ")

       if (move[1] == 'X'):
           sum += play(chr(ord(move[0]) - 1))
       elif (move[1] == 'Y'):
           sum += 3 + play(move[0])
       elif (move[1] == 'Z'):
           sum += 6 + play(chr(ord(move[0]) + 1))
   print(sum)
