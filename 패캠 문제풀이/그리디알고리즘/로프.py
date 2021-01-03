# 문제해결 :
#   로프가 3개일 경우 ( 6 , 11 , 12 ) => 오름차순으로 정렬을 시킨다.
#   젤 작은 로프(6) 로 3개로 나누어서 물체를 들어올릴 경우 , 중량이 가장큰 로프로 물체를 들어올릴 경우 ( 6*3 > 12) 의 max값을 구해 max_weight에 저장
#   반복문을 통하여 그 다음 중량이 적은 로프 (11) 로 이번에는 총 3개에서 -1을 한 2개로 나누어 물체를 들어올릴 경우, 중량이 가장큰 로프로 물체를 들어올릴경우 ( 11*2 > 12)의 max값을 구해 max_weight에 저장
#   이렇게 반복문을 돌아 가장 큰값이 max_weight가 되므로 이 값이 정답이 된다.

import sys

N = int(sys.stdin.readline())
weight_list = []
max_weight = 0
count = N
for _ in range(N):
    weight_list.append(int(sys.stdin.readline()))
weight_list.sort()

for index in range(N):
    weight = max(weight_list[index]*count, weight_list[-1])
    max_weight = max(max_weight,weight)
    count -= 1
print(max_weight)