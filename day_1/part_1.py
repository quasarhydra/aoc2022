print(max([sum([int(i) for i in y]) for y in (x.split('\n') for x in open('input.txt', 'r').read().split('\n\n'))]))