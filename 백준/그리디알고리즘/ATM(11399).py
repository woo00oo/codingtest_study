total = int(input())
arr_time = list(map(int,input().split(' ')))

arr_time.sort()
min_time = 0
all_min_time = 0
for i in arr_time:
    min_time += i
    all_min_time += min_time
print(all_min_time)
