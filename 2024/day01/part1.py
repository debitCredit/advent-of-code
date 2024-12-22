from collections import Counter

file = "input.txt"

lst1, lst2 = [], []

with open(file) as f:
  for line in f:
    d1, d2 = map(int, line.strip().split("   "))
    lst1.append(d1)
    lst2.append(d2)

lst1.sort()
lst2.sort()

total_part1 = sum(abs(n1 - n2) for n1, n2 in zip(lst1, lst2))

print(total_part1)
