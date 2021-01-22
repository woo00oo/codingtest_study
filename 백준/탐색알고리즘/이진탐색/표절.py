#문제풀이 :
#   n번 만큼 반복할 때 이분 탐색을 실시
#   index와 비교하면서 몇번째 인덱스까지 조건에 맞는 최대값인지 탐색한다.
import sys

N = int(sys.stdin.readline().strip())
file_list = sorted(list(map(int,sys.stdin.readline().split())))

count = 0

for index in range(N):
    start = index
    end = N

    while end - start >= 0:
        mid = (start + end) // 2

        if file_list[index] >= file_list[mid]*(0.9):
            start = mid + 1

        else:
            end = mid

    count += end - 1 - index


print(count)
