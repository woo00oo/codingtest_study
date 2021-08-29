'''
expendList는 key를 lock의 (0,0)부터 돌리면서 하나하나 맞춰보기 위해 필요한 배열.

1. expendList의 (0,0)부터 반복문을 돌리면서 자물쇠가 열리는지 체크.

2. key 배열을 회전하지 않고 열리면 true, 열리지 않으면 key 배열을 90도 회전해서 1번을 다시 진행.


'''




# 90도 회전
def rotation(arr):
    return list(zip(*arr[::-1]))


# 자물쇠가 열리는지 체크
def check(startX, startY, key, lock, expendSize, start, end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i - start][j - start]
            if expendList[i][j] != 1:
                return False

    return True


def solution(key, lock):
    start = len(key) - 1  # expendList에서 lock의 시작 지점
    end = start + len(lock)  # expendList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2  # expendList 배열의 크기

    # lock은 고정이고 key가 움직이는거!!!
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendSize, start, end):
                    return True
        key = rotation(key)

    return False
