#문제풀이:
#   투포인터 알고리즘으로 해결 P1, P2 의 초기값을 1,2로 설정
#   어떠한 숫자 N이 입력으로 받아지면 최소 자기자신의 숫자는 조건에 만족함으로 answer의 초기값은 1로 셋팅
#   P1 ~ P2 까지의 합이 Sum이 N이랑 같다면 answer +=1, P1을 1증가하고 P2는 P1 + 1로 다시 셋팅
#   작다면 P2를 1 증가
#   크다면 P1를 1 증가
#   while문은 P1이 N이 아닐때까지 반복한다.

N = int(input())

answer = 1
P1 = 1
P2 = 2
while P1 != N:
    Sum = 0
    for i in range(P1, P2+1):
        Sum += i
    if Sum == N:
        answer += 1
        P1 += 1
        P2 = P1 + 1
    elif Sum < N:
        P2 += 1
    else:
        P1 += 1
print(answer)