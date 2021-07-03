# 문자열을 정렬시키면 사전순으로 정렬이 되기 때문에 비교할 때 모든 수를 비교하는 것이 아닌 i번째와 i+1번째만 비교하면 된다.

t = int(input())

def check():
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1][0:len(numbers[i])]:
            print('NO')
            return
    print('YES')

for _ in range(t):
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(input().strip())
    numbers.sort()
    check()