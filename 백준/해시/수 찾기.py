N = input()
arr_N = set(input().split(' '))
M = input()
arr_M = list(input().split(' '))

for i in arr_M:
    if i in arr_N:
        print('1')
    else:
        print('0')

