import re

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(input())

# transpose the matrix
transposed = zip(*matrix)

# concatenate each row into a string
decoded = ""
for row in transposed:
    decoded += "".join(row)

# remove any non-alphanumeric characters except for spaces
decoded = re.sub(r"[^a-zA-Z0-9\s]+", "", decoded)

# replace consecutive non-alphanumeric characters with a single space
decoded = re.sub(r"[^a-zA-Z0-9\s]{2,}", " ", decoded)

print(decoded)