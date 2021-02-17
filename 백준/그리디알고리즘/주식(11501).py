# 첫번째 방법대로 리스트를 앞에서부터 순회를 하면 시간초과가 계속 떴다.
# 그 이유는 max()메소드의 시간복잡도 때문.
# 하지만 리스트를 뒤에서부터 순회하면 올바르게 통과할 수 있다.
# 단순히 현재 max값 보다 현재 인덱스 값이 더 작다면 그 차이만큼 이익을 더해주면 된다.

import sys

# T = int(sys.stdin.readline().strip())
# for _ in range(T):
#     N = int(sys.stdin.readline().strip())
#     li = list(map(int, sys.stdin.readline().split()))
#
#     answer = 0
#
#     for i in range(N):
#         Max = max(li[i:])
#         if li[i] < Max:
#             answer += (Max-li[i])
#
#     print(answer)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    li = list(map(int, sys.stdin.readline().split()))
    answer = 0
    Max = 0
    for i in range(len(li)-1, -1, -1):
        if li[i] > Max:
            Max = li[i]
        else:
            answer += Max - li[i]
    print(answer)