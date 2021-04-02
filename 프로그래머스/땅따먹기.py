# dp 방식 활용.
# 4가지의 경우에서 max 값을 리턴.
# 1) 마지막 행에서 0열을 밟았을 경우, 1열을 밟았을 경우, 2열을 밟았을 경우, 3열을 밟았을 경우를 따져 더해온 값을 중 max값을 리턴.


def solution(land):

    for i in range(0, len(land)-1):

        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])


    return max(land[len(land)-1])

