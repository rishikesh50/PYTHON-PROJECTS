n = int(input())
words = []
for i in range(n):
    words.append(input().strip('n'))
    
# Count the occurrences of each word
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Output the number of distinct words and their occurrences
print(len(counts))
for word in words:
    if word in counts:
        print(counts[word], end=' ')
        del counts[word]