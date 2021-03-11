# 5KG에 설탕을 빠짐없이 담을 수 있다면(5로 나누어떨어지는 경우) 5로 나눈 몫을 출력
# 5KG에 설탕을 빠짐없이 담을 수 없다면 3KG 봉지 한번 담기 (answer +=1 N - 3)
# N이 0보다 작아지면 -1을 출력하고 프로그램 종료


N = int(input())
answer = 0
while True:
    if (N % 5) == 0:
        answer = answer + (N//5)
        print(answer)
        break
    N = N-3
    answer += 1
    if N < 0:
        print(-1)
        break