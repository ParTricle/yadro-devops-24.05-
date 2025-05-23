import sys
with open(sys.argv[1], 'r') as file:
    for line in file:
        if sys.argv[2] in line:
            print(line, end='')