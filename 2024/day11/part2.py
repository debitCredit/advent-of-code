from collections import defaultdict

# file = "test_input.txt"
file = "input.txt"

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


stones_count = defaultdict(int)
for stone in stones:
    stones_count[stone] += 1


for i in range(75):
    new_stones = defaultdict(int)
    for stone, count in stones_count.items():
        for new_stone in step_stone(stone):
            new_stones[new_stone] += count
    stones_count = new_stones

print(sum(stones_count.values()))