N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
tip_sum = 0

for i in range(N):
    tip = arr[i] - ((i+1) - 1)
    if tip > 0:
        tip_sum += tip

print(tip_sum)
