# TODO: read first line and enumerate
# Read all lines, perform check each element, if 0 keep counter and add required number of new fish

with open('input.txt') as f:
    draw = list(map(int, next(f).strip().split(",")))

print(draw)