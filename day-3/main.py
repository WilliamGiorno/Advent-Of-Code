import re

# Read the contents of data.txt
with open('day-3/data.txt', 'r') as file:
    data = file.read()

    # Define the regex patterns
    mul_pattern = re.compile(r'mul\(\d+,\d+\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')

    # Find all matches in the data
    mul_matches = mul_pattern.findall(data)
    do_matches = do_pattern.findall(data)
    dont_matches = dont_pattern.findall(data)

    # Initialize variables
    result = 0
    enabled = True

    # Split the data into tokens
    tokens = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', data)

    for token in tokens:
        print(token)
        if do_pattern.match(token):
            enabled = True
        elif dont_pattern.match(token):
            enabled = False
        elif mul_pattern.match(token) and enabled:
            # Extract the two numbers from the match
            n, m = map(int, re.findall(r'\d+', token))
            # Calculate the result of the multiplication
            result += n * m

    print("Result: ", result)