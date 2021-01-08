# 1차시도 - 시간초과
# total = int(input())
# arr_rank = [ i+1 for i in range(total)]
# answer = 0
# arr_mis = []
# for _ in range(total):
#     expect = int(input())
#     if expect in arr_rank:
#         arr_rank.remove(expect)
#     else:
#         arr_mis.append(expect)
# for i,j in zip(arr_mis,arr_rank):
#     answer += abs(i-j)
# print(answer)

#2차시도 - 시간초과 => 오름차순 이용
# total = int(input())
# arr_rank = [ i+1 for i in range(total)]
# arr_expect = []
# answer = 0
# for _ in range(total):
#     expect_rank = int(input())
#     arr_expect.append(expect_rank)
# arr_expect.sort()
# for i,j in zip(arr_expect,arr_rank):
#     answer += abs(i-j)
# print(answer)

#3차시도 - 시간초과 => 오름차순 이용
#왜 시간초가가 계속 뜨는지 모르겠다....
# total = int(input())
# arr_expect = []
# answer = 0
#
# for _ in range(total):
#     arr_expect.append(int(input()))
#
# arr_expect.sort()
#
# for i in range(total):
#     answer += abs(arr_expect[i] - (i + 1))
#
# print(answer)

# 문제는 input()함수 -> 대량의 데이터를 연속적으로 입력받을 때는 input() 대신 sys.stdin.readline()을 사용
import sys

total = int(sys.stdin.readline())
arr_expect = []
answer = 0
for i in range(total):
    arr_expect.append(int(sys.stdin.readline()))
arr_expect.sort()
for i in range(total):
    answer += abs(arr_expect[i]-(i+1))
print(answer)

