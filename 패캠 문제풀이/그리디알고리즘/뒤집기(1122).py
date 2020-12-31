# 문제착오

A,B,K = list(map(int,input().split(' ')))

arr_A = [0] * A
arr_B = [1] * B
arr_total = arr_A + arr_B
count = 0

while True:
    if arr_total.count(1) == len(arr_total):
        break
    elif arr_total.count(0) == len(arr_total):   ##case:1
        for i in range(K):
            arr_total[i] = 1
        count += 1
    elif arr_total.count(0) == K:               ## case:3
        for i in range(len(arr_total)):
            if arr_total[i] == 0:
                arr_total[i] = 1
        count += 1
    elif arr_total.count(1) >= K-1:               ## case:2
        arr_total.sort()
        arr_total[0] = 1
        for i in range(len(arr_total)-1,K-2,-1):
            arr_total[i] = 0
        count += 1
    else:
        count = -1
        break

print(count)
