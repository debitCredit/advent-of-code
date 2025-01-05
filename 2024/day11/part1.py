# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  stones = [int(x) for x in f.read().split()]


def blink(stones: list, blinks_count: int) -> list:
  for _ in range(blinks_count):
    new_stones = []
    for stone in stones:
      if stone == 0:
        new_stones.append(1)
      elif len(str(abs(stone))) % 2 == 0:
        stone_str = str(stone)
        first, second = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
        new_stones.extend([int(first), int(second)])
      else:
        new_stones.append(stone * 2024)
    stones = new_stones
  return(new_stones)


print(len(blink(stones, 25)))