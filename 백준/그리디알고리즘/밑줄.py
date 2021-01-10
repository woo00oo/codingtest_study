# 문제해결 :
# 예를 들어 아래와 같이 단어가 5개 있고, m=30 이라고 하면,
#
# abc
# Abc
# aBC
# ABC
# aBc
#
# 그러면 밑줄은 30-15=15개 추가
# 단어가 5개니, 밑줄을 넣을 수 있는 위치(구간)는 4개
#
# 1. 최대한 균등하게 밑줄을 넣어야 하므로, 먼저 각 위치에 밑줄을 15/4=3 개씩 써줌
#
# abc___Abc___aBC___ABC___aBc
#
# 2. 밑줄을 15-4*3= 3개 더 넣어야 함. 밑줄을 넣어서 사전순으로 더 앞이 되는 경우는 소문자 시작 단어의 바로 앞쪽에 넣는 것이고, 이 경우 되도록 앞에 위치한 소문자 시작 단어에 적용하는 것이 좋음
#
# abc 1 Abc 2 aBC 3 ABC 4 aBc
#
# 소문자로 시작하는 단어 앞인 곳은 2,  4이다. 남은 밑줄은 3개니까 이 두 위치에 밑줄 1개씩 넣어준다
#
# abc___Abc____aBC___ABC____aBc
#
# 3. 그래도 남은 밑줄은 어쩔 수 없이 대문자 시작 단어 앞에 넣어야 하는데, 밑줄을 넣으면 사전 순에서 뒤로 밀리게 된다 .
# 그래서 최대한 뒤로 밀리지 않도록, 뒤쪽부터 대문자 시작 단어 앞에 밑줄을 1개씩 넣어준다. 그러한 위치로는 1, 3 이 있는데 남은 밑줄은 1개이므로 3에만 밑줄을 넣어주면 된다
#
# abc___Abc____aBC____ABC____aBc

N, M = list(map(int,input().split()))
voca_list = list()

for _ in range(N):
    voca_list.append(input())

S = M - len(''.join(voca_list))
under_list = [S//(N-1)] * (N-1)

remainder = S % (N-1)

if remainder != 0:
    for i in range(1, N):
        if remainder == 0 :
            break
        if voca_list[i][0] > '_':
            under_list[i-1] += 1
            remainder -= 1

if remainder != 0:
    for i in range(N-1, 0, -1):
        if remainder == 0:
            break
        if voca_list[i][0] < '_':
            under_list[i-1] += 1
            remainder -= 1

answer = list()
answer.append(voca_list[0])
for i in range(1,N):
    answer.append('_' * under_list[i-1])
    answer.append(voca_list[i])

print(''.join(answer))