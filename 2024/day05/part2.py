from functools import cmp_to_key

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  rules_section, updates_section = f.read().strip().split('\n\n')

ordering = [tuple(rule.split("|")) for rule in rules_section.splitlines()]
updates = [line.split(",") for line in updates_section.splitlines()]


def comp_rule(a, b):
  return -1 if (a, b) in ordering else 1 if (b, a) in ordering else 0


total = 0
for update in updates:
  new = sorted(update, key=cmp_to_key(comp_rule))
  if new != update:
    total += int(new[len(new) // 2])

print(total)