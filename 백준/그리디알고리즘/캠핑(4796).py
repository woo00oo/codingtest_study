# 문제해결:
#   나머지를 더할때 무조건 모두 더해주어서 틀린 실수를 하였다.
#   나머지가 L보다 큰 경우에는 L를 더해주도록 해야한다.

case = 1
while True:
    L, P, V = map(int,input().split())
    if L == P == V == 0:
        break

    days = (V // P) * L
    V -= (V // P) * P
    if V >= L:
        days += L
    else:
        days += V

    print("Case %d: %d" % (case, days))
    case += 1
