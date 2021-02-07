# 문제해결 : 최악의 경우 257 * 500 * 500을 반복해 시간초과가 뜸 ( 다른언어는 괜찮은데 파이썬만 시간초과에 걸린다..)

# import sys
#
# N, M, B = map(int, input().split())
# li = list()
# min_time = 100000000000000
# answer = 0
#
#
# for _ in range(N):
#     li.append(list(map(int, sys.stdin.readline().split())))
#
#
# for height in range(257):
#     time = 0
#     V = B
#     no = True
#     for i in range(N):
#         if no:
#             for j in range(M):
#                 if no:
#                     block = li[i][j] - height
#                     if block > 0:
#                         time += 2 * block
#                         V += block
#                     elif block < 0:
#                         if V >= -block:
#                             time += -block
#                             V -= -block
#                         else:
#                             no = False
#                     else:
#                         continue
#                 else:
#                     break
#         else:
#             break
#     if time < min_time and no:
#         min_time = time
#         answer = height
#     if not no:
#         break
# print(min_time, answer)

import sys
inp = sys.stdin.readline
n,m,b = map(int,inp().split())
height = [0]*257
time = []
ans = {}
low = 0
high = 256
for i in range(n):
    x = list(map(int,inp().split()))
    for j in range(m):
        height[x[j]] += 1
for i in range(257):
    if height[i] == 0 and low == i:
        low += 1
    if height[256-i] == 0 and high == 256-i:
        high -= 1
for i in range(low, high+1):
    need = 0
    have = 0
    for j in range(low, i):
        need += (i-j)*height[j]
    for j in range(i+1, high+1):
        have += (j-i)*height[j]
    if need > have+b: continue
    else:
        idx = need + have*2
        time.append(idx)
        ans[idx] = i
fast = min(time)
print(fast, ans[fast])