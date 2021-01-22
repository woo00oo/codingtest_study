K, N = list(map(int,input().split()))
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)
answer = 0
while end - start >= 0:
    mid = (start + end) // 2
    count = 0
    for num in arr:
        count += num // mid
    if N <= count:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

