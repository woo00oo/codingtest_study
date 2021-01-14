# 문제해결 :
#   입력받는 자연수가 100보다 같거나 작은 값이기에 브루트포스 알고리즘으로 해결 가능
#   i를 1부터 1씩 증가하여 입력받은 5개의 자연수로 나누어 떨어지는 경우 (3개 이상) 해당 i가 정답.
N1, N2, N3, N4, N5 = list(map(int,input().split()))

i = 1
while True:
    count = 0
    if i % N1 == 0:
        count += 1
    if i % N2 == 0:
        count += 1
    if i % N3 == 0:
        count += 1
    if i % N4 == 0:
        count += 1
    if i % N5 == 0:
        count += 1

    if count >= 3:
        print(i)
        break
    i += 1