from pyaoc import *
# file = "input.txt"
file = "test_input.txt"

with open(file) as f:
    input_data = f.read()

entry = list(input_data.splitlines())

inr = Grid(rows=mapt(digits, entry), neighbors=neighbors8)
