# 그리디 알고리즘의 대표적인 동전 거스름돈과 매우 유사한 문제.

N, K = list(map(int,input().split()))
coin_list = []
coin_count = 0
for _ in range(N):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
for coin in coin_list:
    coin_count += K // coin
    K %= coin
print(coin_count)