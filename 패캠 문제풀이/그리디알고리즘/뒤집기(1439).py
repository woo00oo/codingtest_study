#내가 푼 문제
#문자열 S의 길이는 100만 이하이므로, 시간복잡도 O(N)에 해결해야하는데 런타임 오류가 뜸.
# S = input()
# arr = []
# count = 0
#
#
# for i in range(len(S)-1):
#     if S[i] != S[i+1]:
#         arr.append(S[i])
#
# if arr[-1] != S[-1]:
#     arr.append(S[-1])
#
# if arr.count('0') > arr.count('1'):
#     count = arr.count('1')
# else:
#     count = arr.count('0')
#
# print(count)

# 해설 코드
# 문자열에 있는 숫자를 모두 0 혹은 모두 1로 만드는 2가지의 경우를 따져 횟수가 더 작은 경우가 정답.
# 1) 모두 1로 만드는 경우
#   -첫번째 원소가 0 일 때,
#   -원소가 1 -> 0 으로 바뀔 때
# 2) 모두 0으로 만드는 경우
#   -첫번째 원소가 1 일 때,
#   -원소가 0->1으로 바뀔 때

S = input()
count0 = 0
count1 = 0

if S[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(len(S)-1):

    if S[i] == '1' and S[i+1] == '0':
        count0 += 1
    elif S[i] == '0' and S[i+1] == '1':
        count1 += 1

print(min(count0,count1))