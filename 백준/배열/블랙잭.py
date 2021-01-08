n, m = map(int,input().split())
array = list(map(int,input().split()))
sum = 0
for x in range(0,n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            if m >= array[x] + array[y] + array[z] > sum:
                sum = array[x] + array[y] + array[z]
print(sum)

# 경우의 수  n(n-1)(n-2) / 3! = 대략 1,000,000번 (조합)
# 3중 반복문을 활용하여 모든 경우의 수를 반복 => 컴퓨터가 충분히 계산 가능한 횟수
# 파이썬은 1초에 2천만개의 연산을 수행 가능함.


