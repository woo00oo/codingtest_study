# 리스트 -> 문자열 변환시 리스트의 모든 원소가 str이어야 한다!
# join() 리스트/튜플 -> 문자열로 변환시켜주는 함수

from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

C = list(permutations(cards, k))
for i in range(len(C)):
    C[i] = ''.join(C[i])
answer = set(C)
print(len(answer))
