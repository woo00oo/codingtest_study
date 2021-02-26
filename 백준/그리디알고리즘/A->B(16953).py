# 숫자 , 문자 잘 구별해서 비교하자

A, B = map(int, input().split())
answer = 0
while True:
    str_B = list(str(B))

    if str_B[-1] == '1': ## <--- 이부분 처음엔 str_B[-1] == 1 이라 해서 오류가 났었다.
        answer += 1
        del str_B[-1]
        B = int(''.join(str_B))

    elif B % 2 != 0:
        print(-1)
        exit(0)
    else:
        B = B // 2
        answer += 1

    if A == B:
        print(answer+1)
        exit(0)
    elif A > B:
        print(-1)
        exit(0)