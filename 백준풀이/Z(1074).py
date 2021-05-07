# 첫번째 시도 : 시간 초과
# 주어진 조건대로 정사각형을 방문하면서 원하는 좌표가 나오면 몇 번째로 방문했는지 출력 하도록 함
# 하지만 n이 15일 경우 2^15 * 2^15의 정사각형이 생겨 O(n)의 시간복잡도로 풀 수 없음
# 모든 사각형은 방문하지 않고 조건을 정해 풀어야 함.

# def search(n,x,y):
#     if n == 1:
#         for i in range(2):
#             for j in range(2):
#                 global answer
#                 if x + i == r and y + j == c:
#                     print(answer)
#                 answer += 1
#     else:
#         search(n-1, x, y)
#         search(n-1,x,y+2**(n-1))
#         search(n-1,x+2**(n-1),y)
#         search(n-1,x+2**(n-1),y+2**(n-1))
#
# N, r, c = map(int, input().split())
# answer = 0
# search(N,0,0)

###-------------------------------------------------------

# 2번째 풀이:
# 조건 : 해당 범위 내에 있는 사각형 안에 찾고자 하는 좌표가 없을 경우 그 범위 내에 있는 총 사각형 수 만큼 방문 횟수에 누적
# 즉 z자로 순회할 필요 없이 해당 사각형 크기 만큼 answer에 더 해주는 방식.

def search(n,x,y):
    global answer
    if x == r and y == c:
        print(int(answer))
        exit(0)
    if n == 1:
        answer += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        answer += n * n
        return

    search(n / 2, x, y)
    search(n / 2, x, y + n / 2)
    search(n / 2, x + n / 2, y)
    search(n / 2, x + n / 2, y + n / 2)

N, r, c = map(int, input().split())
answer = 0
search(2**N,0,0)




