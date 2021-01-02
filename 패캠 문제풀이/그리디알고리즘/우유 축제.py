N = int(input())
milk_list = list(map(int,input().split()))
milk_select = 0
count = 0
for milk in milk_list:
    if milk == milk_select:
        count +=1
        milk_select += 1
    if milk_select == 3:
        milk_select = 0
print(count)