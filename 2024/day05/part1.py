# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  text = f.read().splitlines()

ordering, updates, correct = [], [], []
for i in text:
  if not i: continue
  if "|" in i:
   [a, b] = i.split("|")
   ordering.append([a, b])
  else:
    updates.append(i)

# print(f"{updates=}")

for update in updates:
  numbers = [x for x in update.split(",")]
  pairs = [[numbers[i], numbers[i+1]] for i in range(len(numbers)-1)]
  is_valid = True
  for pair in pairs:
    if pair not in ordering:
      is_valid = False
      break
  if is_valid:
    correct.append(numbers)

total = 0
for item in correct:
  total += int(item[len(item) // 2])


print(total)
