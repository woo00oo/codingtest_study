import sys

N, M = map(int,input().split())
height = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(height)
answer = 0

while end - start >= 0:
    mid = (start + end) // 2
    Sum = 0
    for i in height:
        if i > mid:
            Sum += i - mid
    if Sum >= M:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)