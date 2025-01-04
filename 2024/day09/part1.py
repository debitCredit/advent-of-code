from itertools import cycle


# file = "test_input.txt"
file = "input.txt"

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


def compact(unpacked: list) -> list:
  for i in range(len(unpacked)):
    if unpacked[i] == ".":
      remaining = unpacked[i+1:]
      rev_index, value = next(((i, x) for i, x in enumerate(reversed(remaining)) if x != "."), (None, None))
      if rev_index is not None:
          original_index = len(unpacked) - 1 - rev_index
          unpacked[i], unpacked[original_index] = unpacked[original_index], unpacked[i]
  return unpacked


def checksum_calc(compacted: list) -> int:
  checksum = 0
  for i, data in enumerate(compacted):
    if compacted[i] != ".":
      checksum += i * data
  return checksum


print(checksum_calc(compact(unpack(disk_map))))