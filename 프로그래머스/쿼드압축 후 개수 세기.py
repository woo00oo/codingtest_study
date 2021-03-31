# 처음 풀이:
#   중복해서 cnt를 빼주고 있어 문제에서 원하는 정답을 찾을 수 없었다.
#   전체 0,1의 개수를 구해준 후 행의 길이(l) 8,4,2,1 순으로 반복해서 정사각형 만큼의 길이만큼 숫자가 동일하면 l**2 - 1 을 빼주는 식으로 해결하려고 하였지만
#   l이 4일때 2일때 중복해서 빼주는 방식이라 원하는 정답을 찾을 수 없었음. 중복된 for문으로 시간복잡도 x
#   시작점으로 부터 l만큼 행, 열을 더해주는 방식은 적절한 접근 방법이였음

# def solution(arr):
#     cnt_0, cnt_1 = 0, 0
#     l = len(arr[0])
#
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] == 0:
#                 cnt_0 += 1
#             else:
#                 cnt_1 += 1
#
#     while True:
#         l //= 2
#
#         if l == 1:
#             break
#
#         for i in range(0, len(arr), l):
#             for j in range(0, len(arr[i]), l):
#
#                 same = True
#                 for x in range(i, i+l):
#                     for y in range(j, j+l):
#                         if arr[i][j] != arr[x][y]:
#                             same = False
#
#                 if same:
#                     if arr[i][j] == 0:
#                         cnt_0 -= l**2 - 1
#                     else:
#                         cnt_1 -= l**2 - 1
#
#     answer = list()
#     answer.append(cnt_0)
#     answer.append(cnt_1)
#
#     return answer


# 사각형 중 하나의 값을 초기값으로 잡고 사각형 안의 값을 하나씩 비교해가면서 초기값과 다른게 하나라도 있으면 압축할 수 없으므로 또 그 사각형을 잘라준다.
def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]  # 해당 네모값중 하나 # 모두 같아야 통과임
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  # 한번이라도 다르면 그 네모는 압축불가
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return

        # 무사히 다 통과했다면 압축가능
        answer[init] += 1

    comp(0, 0, N)
    return answer