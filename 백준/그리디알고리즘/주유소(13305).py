# 문제풀이:
#   조건 기름이 없는 상태에서 출발 처음 도시에서는 무조건 기름을 넣어야함
#   각 도시에 도착할때마다 가격을 이전 도시와 비교하여
#   이전 도시가 가격이 낮을 경우에는 d에다가 각 거리를 더해나가고
#   지금 도시가 가격이 낮을 경우에는 더해준 d에다가 가격을 더해준다

N = int(input())
distance = list(map(int, input().split()))
prices = list(map(int, input().split()))
answer = 0
price = prices[0]
d = distance[0]
for i in range(1, N):
    if i == N-1:
        answer += price * d
        break
    if prices[i] > price:
        d += distance[i]
    else:
        answer += price * d
        d = distance[i]
        price = prices[i]

print(answer)

