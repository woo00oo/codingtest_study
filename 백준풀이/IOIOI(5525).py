# 이 문제는 O(N)의 시간복잡도로 해결해야 한다.
# 파이썬 슬라이싱의 시간 복잡도 list[a:b] => O(b-a)의 시간 복잡도를 가지게 된다
# 즉 아래 코드는 O(N^2)이므로 시간초과가 발생

N = int(input())
M = int(input())
S = input()


p = 'IO' * N + 'I'
answer = 0

for i in range(M-len(p)):
    if S[i:i+len(p)] == p:
        answer += 1

print(answer)




## ----------------------------------------
# 문자열 전체를 비교하는 것이 아니라 IOI라는 문자단위로 비교한다
# 인덱스를 2씩 증가 시키면 IOI의 갯수를 세고 그 갯수가 N과 일치하면 answer를 1 증가.

N = int(input())
M = int(input())
S = input()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 2
    else:
        count = 0
        i += 1

# OOIOIOIOIIOII