from sys import stdin
from collections import Counter

N = int(input())
card_list = []
for _ in range(N):
    card_list.append(int(stdin.readline().strip()))

cnt_card_list = list(Counter(card_list).items())
cnt_card_list.sort(reverse=True, key=lambda x: (x[1], -x[0]))

print(cnt_card_list[0][0])
