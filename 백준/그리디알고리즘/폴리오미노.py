# 문제해결: 복잡하게 X의 개수를 하나하나 다 구해주면서 풀었다.
#       파이썬의 replace 함수를 사용하여 간단하게 구현 가능.
# B = input()
# arr = list()
# size = 0
# for i in range(len(B)):
#     if B[i] == '.':
#         arr.append(B[i])
#         size = 0
#     else:
#         size += 1
#         if i == len(B) - 1:
#             arr.append(size)
#         elif B[i+1] == '.':
#             arr.append(size)
#
# for i in range(len(arr)):
#     if arr[i] != '.':
#         if arr[i] % 2 == 0 :
#             arr[i] = 'AAAA' * (arr[i] // 4) + 'BB' * (arr[i] % 4 // 2)
#         else:
#             print(-1)
#             exit(0)
# print(''.join(arr))


board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
else:
    print(board)

