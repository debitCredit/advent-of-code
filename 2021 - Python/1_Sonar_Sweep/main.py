with open('input.txt', 'r') as f:
    input_data = f.read()

measurements = list(map(int, input_data.splitlines()))


def part1(data: list) -> int:
    return sum(b > a for a, b in zip(data, data[1:]))


# This works because a + b + c < b + c + d can be reduced to a < b
def part2(data: list) -> int:
    return sum(b > a for a, b in zip(data, data[3:]))


print(part1(measurements))
print(part2(measurements))
