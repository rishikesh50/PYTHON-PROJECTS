from fractions import Fraction
from functools import reduce

n = int(input())
nums = [Fraction(*map(int, input().split())) for _ in range(n)]

product = reduce(lambda x, y: x * y, nums)

print(product.numerator, product.denominator)