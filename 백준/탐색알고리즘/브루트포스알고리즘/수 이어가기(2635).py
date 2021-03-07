# 무한 루프에 빠지지 않게 변수가 어떻게 변화하는지 정확하게 파악하자. 실수 하지 말자

number = int(input())
answer = 2
answer_li = list()

for num in range(1, number+1):
    cnt = 2
    li = list()
    n1 = number
    n2 = num
    li.append(n1)
    li.append(n2)
    while True:
        next_num = n1 - n2
        if next_num < 0:
            break
        li.append(next_num)
        n1 = n2
        n2 = next_num
        cnt += 1
    if answer < cnt:
        answer = cnt
        answer_li = li

print(answer)
print(*answer_li)