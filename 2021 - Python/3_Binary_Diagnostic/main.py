from collections import Counter

with open('input.txt') as f:
    input_data = f.read()

diagnostic = list(input_data.splitlines())


def extract(lst: list, pos):
    return [item[pos] for item in lst]


a = []
gamma_rate_bin = []

for i in range(12):
    a.insert(i, extract(diagnostic, i))

for n in a:
    for k, v in (Counter(n).most_common(1)):
        gamma_rate_bin.append(k)

gamma_rate_string = "".join(gamma_rate_bin)

epsilon_rate_bin = ["1" if x == "0" else "0" for x in gamma_rate_bin]
epsilon_rate_string = "".join(epsilon_rate_bin)

# Part 1
print(f"Part1: {int(epsilon_rate_string, 2) * int(gamma_rate_string, 2)}")

# Part 2



