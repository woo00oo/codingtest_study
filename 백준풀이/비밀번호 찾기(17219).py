import sys

N, M = map(int, input().split())
memo = dict()

for _ in range(N):
    address, pw = sys.stdin.readline().strip().split()
    memo[address] = pw

for _ in range(M):
    address = sys.stdin.readline().strip()
    print(memo[address])