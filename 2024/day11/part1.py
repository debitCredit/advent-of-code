from itertools import chain

file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
  stones = [int(x) for x in f.read().split()]


def step_stone(s: int) -> list[int]:
  if s == 0:
    return [1]
  
  if len(str(s)) % 2 == 0:
    stone_str = str(s)
    first, second = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
    return [int(first), int(second)]
  
  return [s * 2024]

for _ in range(25):
  stones = chain.from_iterable(map(step_stone, stones))


print(len(list(stones)))