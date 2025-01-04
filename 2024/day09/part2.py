from itertools import cycle


file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
  disk_map = [int(x) for x in list(f.read().strip())]


def unpack(disk_map: list) -> list:
  data_type = cycle(["file", "free_space"])
  unpacked = []
  data_index = 0
  for i, data in enumerate(disk_map):
    dtype = next(data_type)
    if dtype == "file":
      unpacked.extend([data_index] * data)
      data_index += 1
    else:
      unpacked.extend(["."] * data)
  return unpacked


def find_blocks(lst, val):
    block, blocks = [], []

    for i, x in enumerate(lst):
        if x == val:
            block.append(i)
        elif block:
            blocks.append(block)
            block = []
    if block:
        blocks.append(block)
    return blocks


def find_spaces(lst, size):
    space, spaces = [], []
    for i, x in enumerate(lst):
        if x == '.':
            space.append(i)
        elif space:
            if len(space) >= size:
                spaces.append(space)
            space = []
    if space and len(space) >= size:
        spaces.append(space)
    return spaces


def compact_ordered(unpacked: list) -> list:
    max_num = max(x for x in unpacked if x != '.')
    
    for num in range(max_num, -1, -1):
        for block in find_blocks(unpacked, num):
            for space in find_spaces(unpacked, len(block)):
                if space[0] < block[0]:
                    for i, pos in enumerate(block):
                        unpacked[space[i]] = num
                        unpacked[pos] = '.'
                    break
    return unpacked

def checksum_calc(compacted: list) -> int:
  checksum = 0
  for i, data in enumerate(compacted):
    if compacted[i] != ".":
      checksum += i * data
  return checksum

print(checksum_calc(compact_ordered(unpack(disk_map))))