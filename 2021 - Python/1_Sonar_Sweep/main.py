def count_increments(input_data):
    """
    Takes a list of values and calculates how many increments between consecutive values there are.
    :return: List
    """
    increments = 0
    previous_line = input_data[0]
    for n in input_data:
        if n > previous_line:
            increments += 1
        previous_line = n
    return increments


with open('input.txt', 'r') as f:
    input_data = f.read()


measurements = [int(x) for x in input_data.splitlines()]
summed_windows = [sum(x) for x in zip(measurements, measurements[1:], measurements[2:])]

# Answer for the first part:
print(f"Answer for the first part: {count_increments(measurements)}")
# Answer for the second part:
print(f"Answer for the second part: {count_increments(summed_windows)}")
