from collections import Counter

file = "input.txt"

lst1, lst2 = [], []

with open(file) as f:
  for line in f:
    d1, d2 = map(int, line.strip().split("   "))
    lst1.append(d1)
    lst2.append(d2)

running_total_second = 0
count_second = Counter(lst2)

for i in lst1:
  running_total_second += i * count_second[i]

print(running_total_second)