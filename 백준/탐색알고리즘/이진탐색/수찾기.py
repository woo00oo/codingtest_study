N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))

for n in M_list:
    start = 0
    end = N-1
    find = False
    while end - start >= 0 :
        mid = (start + end) // 2
        if N_list[mid] == n:
            find = True
            print('1')
            break
        elif N_list[mid] > n :
            end = mid - 1
        else:
            start = mid + 1
    if not find:
        print('0')