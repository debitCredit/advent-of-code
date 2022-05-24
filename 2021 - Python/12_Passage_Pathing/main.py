from collections import defaultdict

file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    input_data = f.readlines()

cave_network = defaultdict(list)

for line in input_data:
    u, v = line.strip().split("-")
    cave_network[u].append(v)
    cave_network[v].append(u)


def dfs(caves, cave, seen, part2=False):
    if cave == "end":
        return 1
    ans = 0
    for c in caves[cave]:
        if c not in seen:
            tmp = {c} if c.islower() else set()
            ans += dfs(caves, c, seen | tmp, part2)
        elif part2 and c != "start":
            ans += dfs(caves, c, seen, False)
    return ans


print(dfs(cave_network, "start", {"start"}))
print(dfs(cave_network, "start", {"start"}, True))
