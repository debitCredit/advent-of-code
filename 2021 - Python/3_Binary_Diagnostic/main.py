from collections import Counter

with open('input.txt') as f:
    input_data = f.read()

diagnostic = list(input_data.splitlines())


def extract_nth(lst: list, pos: int) -> list:
    return [i[pos] for i in lst]


a = []
gamma_rate_bin = []

for i in range(12):
    a.insert(i, extract_nth(diagnostic, i))

for n in a:
    for k, v in (Counter(n).most_common(1)):
        gamma_rate_bin.append(k)

gamma_rate_string = "".join(gamma_rate_bin)

e_rate = "".join(["1" if x == "0" else "0" for x in gamma_rate_bin])

print(f"Part1: {int(e_rate, 2) * int(gamma_rate_string, 2)}")  # 4006064


# Part 2
def calc_common(lst: list, oxygen=True, most=True) -> str:
    r = Counter(lst).most_common(2)
    if len(r) != 1:
        if r[0][1] == r[1][1] and oxygen:
            return "1"
        elif r[0][1] == r[1][1] and not oxygen:
            return "0"
    return r[0][0] if most else r[1][0]


a = diagnostic
for n in range(12):
    if len(a) > 1:
        b = extract_nth(a, n)
        a = [i for i in a if calc_common(b) == i[n]]

u = diagnostic
for n in range(12):
    if len(u) > 1:
        b = extract_nth(u, n)
        u = [i for i in u if calc_common(b, False, False) == i[n]]


print(f"Part2: {int(*a, 2) * int(*u, 2)}")

