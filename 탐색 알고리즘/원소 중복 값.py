from collections import Counter

arr = [2,7,7,7,1,7,2]
counter_arr = list(Counter(arr).items())
max_counter_num = max(counter_arr,key=lambda x: x[1])[0]
if max_counter_num > len(arr) // 2:
    print(max_counter_num)
else:
    print(-1)