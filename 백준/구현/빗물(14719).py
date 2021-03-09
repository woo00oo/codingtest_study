# 문제풀이:
#   2차원 배열을 활용하여 문제를 해결할 수 있다.
#   입력을 받을 때 블록이 쌓이 높이를 받아오기 때문에 이를 활용해 2차원 배열을 0 또는 1(블록)으로 변환시켜줘야한다.
#   그 후에 가장 아래부터(i를 반대로) 반복문을 돌면서 0일경우(비어있는 경우)를 리스트에다가 해당 j를 저장시켜준다.
#   처음에는 왼쪽벽 하나 오른쪽벽 하나로 생각하여 2번째 테스트케이스가 풀리지 않았다. 즉, 벽이 여러개 일수도있다
#   가장 왼쪽벽의 위치와 가장 오른쪽벽의 위치만 구해주면 그 해당하는 범위(left < w < right)가 빗물이 고일수 있게된다
#   전체 행을 반복하여 answer의 그수를 더해주면 문제를 해결할 수 있게 된다.

H, W = map(int,input().split())
W_li = list(map(int,input().split()))
my_map = list()
answer = 0
for _ in range(H):
    my_map.append([0]*W)
for i in range(H-1,-1,-1):
    height = H - i
    for j in range(W):
        if height <= W_li[j]:
            my_map[i][j] = 1

for i in range(H-1,-1,-1):
    left, right = -1, -1
    cnt = list()
    for j in range(W):
        if my_map[i][j] == 1:
            if left == -1:
                left = j
            else:
                right = j
        else:
            cnt.append(j)

    for w in cnt:
        if left < w < right:
            answer += 1

print(answer)