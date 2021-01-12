N = int(input())
height_list = list()
for _ in range(N):
    height_list.append(int(input()))
left_count = 1
right_count = 1
left_max = height_list[0]
right_max = height_list[-1]

for i in range(1,N):
    if left_max < height_list[i]:
        left_max = height_list[i]
        left_count += 1
for i in range(N-2,-1,-1):
    if right_max < height_list[i]:
        right_max = height_list[i]
        right_count += 1
print(left_count)
print(right_count)