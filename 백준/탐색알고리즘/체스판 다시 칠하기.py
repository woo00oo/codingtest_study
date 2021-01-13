#문제 해결 능력:
#   N,M이 8 초과인 경우는 행과 열을 움직여가며 8 * 8 체스판 규칙에 어긋난 갯수를 구해야 한다.
#   그중 가장 적게 어긋난 갯수를 반환해주면 정답.

#   *왼쪽 위 칸이 흰색인 경우
# 행 인덱스 짝수 and 열  인덱스 짝수 면  ==> W
# 행 인덱스 홀수 and 열  인덱스 홀수 면  ==> W
# 행 인덱스 홀수 and 열  인덱스 짝수 면  ==> B
# 행 인덱스 짝수 and 열  인덱스 홀수 면  ==> B

#   *왼쪽 위 칸이 검정색인 경우
# 행 인덱스 짝수 and 열  인덱스 짝수 면  ==> B
# 행 인덱스 홀수 and 열  인덱스 홀수 면  ==> B
# 행 인덱스 홀수 and 열  인덱스 짝수 면  ==> W
# 행 인덱스 짝수 and 열  인덱스 홀수 면  ==> W


def check_BW(matrix):
    case1_not_match = 0
    case2_not_match = 0

    # case 1 시작점(0,0)이 W 인경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "W":
                    case1_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "B":
                    case1_not_match += 1

    # case 2 시작점(0,0)이 B 인경우 
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "B":
                    case2_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "W":
                    case2_not_match += 1

    return min(case1_not_match, case2_not_match)


def solution():
    input_list = []
    N, M = list(map(int,input().split()))
    for idx in range(N):
        input_list.append(list(input()))

    min_revise_cnt = 9999999999999999999

    for row in range(N - 7):
        for col in range(M - 7):
            # 8*8 매트릭스로 자르기
            slice_mat = [one_row[col:col + 8] for one_row in input_list[row:row + 8]]
            revise_cnt = check_BW(slice_mat)
            min_revise_cnt = min(min_revise_cnt, revise_cnt)

    return min_revise_cnt


print(solution())