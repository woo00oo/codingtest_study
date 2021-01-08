price = int(input())

change = 1000 - price
coin_list = [500,100,50,10,5,1]
total_coin_count = 0

for coin in coin_list:
    coin_num = change // coin
    total_coin_count += coin_num
    change -= coin * coin_num

print(total_coin_count)