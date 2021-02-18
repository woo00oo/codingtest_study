# 1차시도 : 모든 조합을 리스트로 구해준다음 주어진 M을 찾아서 빼주는 방식으로 접근하였지만, 시간초과

# from itertools import combinations
# import sys
#
#
# N, M = map(int, sys.stdin.readline().split())
# numbers = [i for i in range(1, N+1)]
# li = list()
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     li.append((a, b))
# ex = list(combinations(numbers, 3))
# for i in li:
#     cnt = 0
#     for j in range(len(ex)):
#         j -= cnt
#         if i[0] in ex[j] and i[1] in ex[j]:
#             del ex[j]
#             cnt += 1
# print(len(ex))

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, N+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)