# 시간 복잡도 : O(n^2) -> 시간초과
# count 메서드 -> O(N)

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
answer = []

for num in numbers:
    answer.append(cards.count(num))

print(*answer)

# -----------------------
# 시간복잡도 O(N)
# 딕셔너리 자료구조 활용 ( 해싱 검색속도 빠름 O(1) )

N = int(input())
cards = list(map(int, input().split()))
cards_dict = dict()
M = int(input())
numbers = list(map(int, input().split()))
answer = []
for card in cards:
    if card not in cards_dict:
        cards_dict[card] = 1
    else:
        cards_dict[card] += 1

for num in numbers:
    if num in cards_dict:
        answer.append(cards_dict[num])
    else:
        answer.append(0)

print(*answer)
