n, m = list(map(int,input().split()))
card_list = sorted(list(map(int,input().split())))

while m:
    m -= 1
    merge = card_list[0] + card_list[1]
    card_list[0] = merge
    card_list[1] = merge
    card_list.sort()


print(sum(card_list))