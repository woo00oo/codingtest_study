X, Y = list(map(int,input().split()))
Z = (Y * 100) // X
start = 1
end = X
answer = 9999999999999999999999

while end - start >= 0:
    mid = (start + end) // 2
    up_Z = ((Y + mid) * 100) // (X + mid)

    if up_Z > Z:
        if answer > mid:
            answer = mid
        end = mid - 1
    else:
        start = mid + 1

if answer == 9999999999999999999999:
    answer = -1
print(answer)
