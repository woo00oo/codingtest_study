# 내 풀이:
#   4가지의 경우(구성이 같거나, 더하거나, 빼거나, 바꾸는)를 충족하는 경우 answer += 1을 하였지만, 단어를 체크하는 과정 중복된 경우는 따지지 않아 문제를 해결하지 못함
#   Counter이라는 라이브러리를 활용하여 문제 풀이.
#   coolections 모듈의 Counter 클래스 => 어떤 단어가 주어졌을 때 단어의 포함된 각 알파벳의 글자 수를 세어주는 간단한 모듈
# N = int(input())
# words = list()
# answer = 0
# for _ in range(N):
#     word = list(input())
#     word.sort()
#     words.append(word)
#
#
# for i in range(1, N):
#     if words[0] == words[i]:
#         answer += 1
#     elif len(words[0]) == len(words[i]):
#         cnt = 0
#         for j in range(len(words[i])):
#             if words[i][j] in words[0]:
#                 cnt += 1
#         if cnt - 1 == len(words[0]):
#             answer += 1
#     elif len(words[0]) + 1 == len(words[i]):
#         cnt = 0
#         for j in range(len(words[0])):
#             if words[i][j] in words[0]:
#                 cnt += 1
#         if cnt == len(words[0]):
#             answer += 1
#     elif len(words[0]) == len(words[i]) + 1:
#         cnt = 0
#         for j in range(len(words[i])):
#             if words[i][j] in words[0]:
#                 cnt += 1
#         if cnt == len(words[i]):
#             answer += 1
#
# print(answer)


#######################

from collections import Counter


N = int(input())
s = Counter(input())
answer = 0

for _ in range(N - 1):
    c = Counter(input())

    if sum((s - c).values()) <= 1 and sum((c - s).values()) <= 1:
        answer += 1

print(answer)

### 딕셔너리 관리 함수
# a.values() => Value 리스트 만들기
# a.keys() => Key 리스트 만들기
# a.items() => (Key,Value) 리스트 만들기