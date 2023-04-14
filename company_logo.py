from collections import Counter

if _name_ == '_main_':
    s = input().strip()
    counter = Counter(s)
    top_three = counter.most_common(3)
    for char, count in top_three:
        print(char, count)