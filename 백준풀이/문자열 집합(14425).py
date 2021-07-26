import sys

N, M = map(int, input().split())

s_set = set()
s_find = list()

for _ in range(N):
    s = sys.stdin.readline().strip()
    s_set.add(s)

for _ in range(M):
    s = sys.stdin.readline().strip()
    s_find.append(s)

answer = 0
for s in s_find:
    if s in s_set:
        answer += 1

print(answer)
