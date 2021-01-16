#문제 해결 능력:
# 문자열의 길이에서 2씩 줄이며 조건을 만족하는지 확인한다.

import sys
# 왼쪽 N자리 합과 오른쪽 N자리 합이 같은지 확인
def isLucky(x):
    mid = len(x) // 2
    sum1 = sum(x[:mid])
    sum2 = sum(x[mid:])
    if sum1 == sum2:
        return True
    else:
        return False

def solution(arr):
    # 문자열이 짝수인경우
    if len(arr) % 2 == 0:
        chk = len(arr)
    # 문자열이 홀수인경우
    else:
        chk = len(arr) - 1
    while chk > 0:
        i = 0
        ans = 0
        while i + chk <= len(arr):
            # 행운의 티켓이면 반복문 종료
            if isLucky(arr[i:i + chk]):
                ans = chk
                return ans
            i += 1
        chk -= 2
    return 0


s = list(map(int, list(sys.stdin.readline().strip())))
print(solution(s))

