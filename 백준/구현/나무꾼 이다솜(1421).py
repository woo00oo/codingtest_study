#문제해결 :
#   브루트포스 알고리즘을 해결
#   전체 탐색 범위를 1~가장큰 나무길이로 잡아야한다.

# N, C, W = map(int,input().split())
# li = [int(input()) for _ in range(N)]
# max_total = 0
# for index in range(N):
#     L = li[index]
#     while L:
#         K = 0
#         cut = 0
#         for i in range(N):
#             if li[i] >= L:
#                 K += li[i] // L
#                 if li[i] % L == 0:
#                     cut += li[i] // L - 1
#                 else:
#                     cut += li[i] // L
#         total = L * K * W - C*cut
#         if max_total < total:
#             max_total = total
#         L -= 1
# print(max_total)

N, C, W = map(int, input().split())
li = [int(input()) for _ in range(N)]
max_total = 0

for L in range(1, max(li) + 1):
    count = 0
    for wood in li:
        K = wood // L
        if wood % L == 0:
            cut = wood // L - 1
        else:
            cut = wood // L
        if K * W * L - cut * C > 0: #자르는 비용이 조각을 팔았을때 보다 더 든다면(음수일경우) 그 나무는 아예 안팔아어 버리는게 맞음.
            count += K * W * L - cut * C
    max_total = max(max_total, count)

print(max_total)