#문제 해결 :
# 넣어야 할 밑줄의 개수는 s=m-(단어 길이의 총합)
#
# 1. 일단 밑줄을 단어 사이에 균등하게 분배 (단어가 n개면 구간은 n-1개)
# 즉, 각 단어 사이에 s/(n-1) 개의 밑줄을 쓴다.
# 2. 이제 남은 밑줄 개수는 s%(n-1)개.
# 남은 밑줄을 앞쪽에서부터 소문자로 시작하는 단어의 앞쪽에 1개씩 최대한 배치. (맨 앞 단어는 제외)
# 3. 이렇게 하고 나서도 남은 밑줄이 있으면 뒤쪽에서부터 대문자로 시작하는 단어의 앞에 1개씩 최대한 배치. (맨 앞 단어는 제외)


# 제시된 테스트 케이스는 풀리지만 모든 테스트를 성공하는데는 실패...

n, m = list(map(int,input().split()))
voca_list = list()
a = list()

for i in range(n):
    voca = input()
    m -= len(voca)
    voca_list.append(voca)
    if voca[0] > '_':
        a.append(voca)
    if i != n-1:
        voca_list.append('_')
        m -= 1


for value in a:
    if m == 0:
         break
    index = voca_list.index(value)
    if index != 0:
        voca_list.insert(voca_list.index(value), '_')
        m -= 1

index = len(voca_list) - 1
while m:
    if voca_list[index] != '_':
        voca_list.insert(index, '_')
        m -= 1
    index -= 1

print(''.join(voca_list))