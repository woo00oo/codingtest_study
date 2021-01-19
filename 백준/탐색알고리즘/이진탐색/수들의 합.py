# 문제해결 :
#   S의 범위가 너무나도커 이진 탐색으로 풀려고 시도.
#   이진탐색으로 해결하지 못하여 브루트포스 알고리즘을 활용하여 풀었더니 통과.
N = int(input())

i = 1
sum_num = 0
count = 0
while N - sum_num >= 0:
    sum_num += i
    i += 1
    count += 1

print(count-1)
