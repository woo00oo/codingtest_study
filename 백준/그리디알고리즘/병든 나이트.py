#문제풀이 :
#   나이트는 좌측으로 가지 않고 반드시 우측으로 이동.
#   이동 횟수가 4보다 적은 경우와 4번 이상의 경우를 나눠서 처리( 최소 3*7 이상의 체스판이여야함 )

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
elif m < 7:
    print(min(4, m))
else:
    print(m - 7 + 5)