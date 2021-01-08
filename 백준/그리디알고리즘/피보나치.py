fibo_list = [0,1]
while True:
    if fibo_list[-1] > 1000000000:
        break
    fibo_list.append(fibo_list[-1] + fibo_list[-2])

T = int(input())

for _ in range(T):
    num = int(input())
    answer_list = list();
    while num:
        for index in range(len(fibo_list)):
            if fibo_list[index] <= num:
                max_num = fibo_list[index]
        num -= max_num
        answer_list.append(max_num)

    answer_list.sort()
    for i in range(len(answer_list)):
        print(answer_list[i],end=' ')
