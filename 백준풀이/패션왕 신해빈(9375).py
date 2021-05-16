T = int(input())

for _ in range(T):
    n = int(input())
    clothes = dict()
    answer = 1

    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 2 # 초기값을 2로 두는 이유 : 해당 옷을 안입은 경우도 따지기 위해

    clothes = list(clothes.items())

    for i in range(len(clothes)):
        answer *= clothes[i][1]

    print(answer - 1) # 모든 옷을 안입은 경우는 제외
