# Read the contents of data.txt
with open('day-1/data.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.splitlines()

# Initialize lists for left and right values
left_values = []
right_values = []

# Process each line
for line in lines:
    left, right = line.split()
    left_values.append(int(left))
    right_values.append(int(right))

# Sort the lists
left_values.sort()
right_values.sort()

# Calculate the absolute differences
differences = sum(abs(l - r) for l, r in zip(left_values, right_values))

print("Differences:", differences)

# Count occurrences of left values in right values
occurrences_sum = 0
for left in left_values:
    count = right_values.count(left)
    occurrences_sum += left * count

print("Occurrences Sum:", occurrences_sum)