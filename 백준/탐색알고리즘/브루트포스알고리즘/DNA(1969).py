#문제풀이 :
#   1차시도(실패) : 중복순열(itertools.product)을 이용하여 모든 DNA의 경우의 수를 구해서 입력값으로 받아진 DNA들의 HD가 최소로 구해질때마다 리스트를 삭제하는 방식으로 접근
#   문자열의 길이가 50일 경우 모든 경우의수는 4^50 이므로 너무나 큰수가 구해진다
#   2차 시도:
#   가장 많이 등장하는 문자를 세고 그 값을 Max로 설정
#   가장 많이 등장하는 문자를 HD가 최소가 되도록 하므로 DNA결과(answer)에 포함시킨다
#   하나의 뉴클레오티드가 결정될 때마다 HD값은 N - Max만큼 증가.

N, M = map(int,input().split())
DNA = list()
answer = ''
HD = 0
for i in range(N):
    DNA.append(input())

for i in range(M):
    cnt = [0,0,0,0]
    for j in range(N):
        if DNA[j][i] == 'A':
            cnt[0] += 1
        elif DNA[j][i] == 'C':
            cnt[1] += 1
        elif DNA[j][i] == 'G':
            cnt[2] += 1
        elif DNA[j][i] == 'T':
            cnt[3] += 1

    Max = max(cnt)
    idx = cnt.index(Max)
    if idx == 0:
        answer += 'A'
    elif idx == 1:
        answer += 'C'
    elif idx == 2:
        answer += 'G'
    elif idx == 3:
        answer += 'T'
    HD += N - Max
print(answer)
print(HD)