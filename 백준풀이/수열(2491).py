# N의 범위가 1이상이기 때문에 increase와 decrease를 1로 초기화 해준다!
# 항상 N의 범위를 잘 체크하여 예외처리를 확실히 해주는 습관을 가지도록 하자

N = int(input())
numbers = list(map(int, input().split()))

increase = 1
decrease = 1
in_cnt = 1
de_cnt = 1
# 증가
for i in range(N-1):
    if numbers[i] <= numbers[i+1]:
        in_cnt += 1
    else:
        in_cnt = 1

    if increase < in_cnt:
        increase = in_cnt
# 감소
for i in range(N-1):
    if numbers[i] >= numbers[i+1]:
        de_cnt += 1
    else:
        de_cnt = 1

    if decrease < de_cnt:
        decrease = de_cnt

if decrease > increase:
    print(decrease)
else:
    print(increase)