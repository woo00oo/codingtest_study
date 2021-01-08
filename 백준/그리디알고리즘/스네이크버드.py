N, height = list(map(int,input().split()))
fruit_list = sorted(list(map(int,input().split())))

max_height = height

for fruit in fruit_list:
    if max_height >= fruit:
        max_height += 1
    else:
        break

print(max_height)
