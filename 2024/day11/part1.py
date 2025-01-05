# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  stones = [int(x) for x in f.read().split()]


def blink(stones: list, blinks_count: int):
  for _ in range(blinks_count):
    new_list = []
    for i, stone in enumerate(stones):
      if stone == 0:
        new_list.append(1)
      elif len(str(abs(stone))) % 2 == 0:
        stone_str = str(stone)
        first, second = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
        new_list.extend([int(first), int(second)])
      else:
        new_list.append(stone * 2024)
        stones = new_list
  return(new_list)


print(len(blink(stones, 25)))