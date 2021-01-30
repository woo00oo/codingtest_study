# round 함수 => 반올림 해주는 함수, 2번째 인자에 소수 몇번째 자리 나타낼 것인지 나타냄


N, M, K = map(int,input().split())
arr = list()
answer = list()

for _ in range(M):
    S = list(map(float,input().split()))
    for index in range(0, 2*N, 2):
        i, s = S[index], S[index+1]
        arr.append((int(i),s))
arr.sort(key=lambda x:x[1],reverse=True)
count = 0
a = 0.0
while count < K and arr:
    value = arr.pop(0)
    if value[0] not in answer:
        count += 1
        a += value[1]
        answer.append(value[0])

print(round(a, 1))
