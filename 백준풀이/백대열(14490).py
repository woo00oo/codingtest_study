from math import gcd

n, m = map(int, input().split(':'))
number = gcd(n, m)

print(n // number, end="")
print(':', end="")
print(m // number)
