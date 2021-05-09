# heapq 라이브러리 활용.
# heap이 0인 경우에서 push 메소드를 사용하게 되면 IndexError 예외가 발생
# try except문을 사용하여 처리
# input()으로 대량의 입력값을 받을 경우 시간초과가 발생 -> sys.stdin.readline() 활용


import heapq
import sys

heap = []
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        try:
            max_num = heapq.heappop(heap)[1]
            print(max_num)
        except:
            print(0)