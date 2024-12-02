# The levels are either all increasing or all decreasing.
def is_incraesing_or_decreasing(line):
    numbers = list(map(int, line.split()))
    # Check for duplicates
    if len(numbers) != len(set(numbers)):  
        return False
    ascending = sorted(numbers) == numbers
    descending = sorted(numbers, reverse=True) == numbers
    return ascending or descending


# Any two adjacent levels differ by at least one and at most three
def is_difference_between_numbers_correct(line):
    numbers = list(map(int, line.split()))
    # Check that the difference between the numbers is between 1 and 3
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) > 3:
            return False
    return True


# If removing a single number from an unsafe line would make it safe, the line instead counts as safe
def is_removing_number_safe(line):
    numbers = list(map(int, line.split()))
    for i in range(len(numbers)):
        # Remove the number at index i
        new_numbers = numbers[:i] + numbers[i + 1:]
        if is_incraesing_or_decreasing(' '.join(map(str, new_numbers))) and is_difference_between_numbers_correct(' '.join(map(str, new_numbers))):
            return True
    return False


# Read the contents of data.txt
with open('day-2/data.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.splitlines()

# Initialize a counter for correct lines
correct_lines = 0
for line in lines:
    if is_incraesing_or_decreasing(line) and is_difference_between_numbers_correct(line):
        correct_lines += 1
    elif is_removing_number_safe(line):
        correct_lines += 1

print("Number of safe reports: ", correct_lines)
