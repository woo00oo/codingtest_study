# 무조건 가운데 있는 것이 가장 작은 거리 값을 갖는다.

N = int(input())
li = sorted(list(map(int, input().split())))

print(li[(N-1)//2])
