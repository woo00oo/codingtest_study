T = int(input())
coins = [25,10,5,1]
for _ in range(T):
    answer = list()
    C = int(input())
    for coin in coins:
        answer.append(C // coin)
        C %= coin
    print(*answer)