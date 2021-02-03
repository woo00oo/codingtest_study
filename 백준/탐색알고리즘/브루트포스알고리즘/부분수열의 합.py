# 조합 : itertools의 combination을 사용


from itertools import combinations

N, S = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in range(1,N+1):
    answer = list(combinations(arr,i))

    for index in range(len(answer)):
        sum_num = sum(answer[index])
        if sum_num == S:
            count += 1

print(count)

