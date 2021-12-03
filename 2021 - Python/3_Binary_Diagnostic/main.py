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

print(f"Part1: {int(epsilon_rate_string, 2) * int(gamma_rate_string, 2)}")  # 4006064

# Part 2

# extract nth elements of the lists in list of lists


def extract_nth(lst: list, pos: int) -> list:
    return [i[pos] for i in lst]


def calc_most_common(lst: list, oxygen=True) -> str:
    r = Counter(lst).most_common(2)
    if r[0][1] == r[1][1] and oxygen:
        return "1"
    elif r[0][1] == r[1][1] and not oxygen:
        return "0"
    return r[0][0]





