# 문제풀이 : 반복문을 통해 1부터 입력을 받은 수가 나올때까지 반복
# 주의 : now_e = (now_e + 1) % 16와 같이 나머지 연산자를 사용하게 되면
# now_e가 15일 때 0으로 연산이 되기 때문에 if문을 사용하여 처리해준다.

E, S, M = map(int, input().split())

now_e, now_s, now_m = 1, 1, 1
year = 1

while True:
    if now_e == E and now_s == S and now_m == M:
        break

    now_e += 1
    now_s += 1
    now_m += 1
    year += 1

    if now_e >= 16:
        now_e -= 15
    if now_s >= 29:
        now_s -= 28
    if now_m >= 20:
        now_m -= 19

print(year)

## 중국인의 나머지 정리를 활용한 풀이

E, S, M = map(int, input().split())
year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1
