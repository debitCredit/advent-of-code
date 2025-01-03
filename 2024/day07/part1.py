from itertools import product

# file = "test_input.txt"
file = "input.txt"
chars = ["*", "+"]

def _evaluate_line(num_seq: list, test_val: int):
  operations = [op for op in product(chars, repeat=len(num_seq) - 1)]

  for op in operations:
    result = num_seq[0]
    for i in range(len(op)):
      if op[i] == "+":
        result += num_seq[i + 1]
      elif op[i] == "*":
        result *= num_seq[i + 1]
    if result == test_val:
      return test_val
  return 0


total = 0
with open(file) as f:
  for l in f:
    test_val, num_seq = l.split(": ")
    num_seq = [int(n) for n in num_seq.split()]
    test_val = int(test_val)
    total += _evaluate_line(num_seq, test_val)

print(total)
