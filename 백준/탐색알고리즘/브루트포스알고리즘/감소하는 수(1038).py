# 시간 초과

N = int(input())
i = 11
answer = 10

if N <= 10:
    print(N)
    exit(0)

while True:
    number = list(str(i))
    d_number = sorted(number,reverse=True)
    s_number = set(number)
    if d_number == number and len(s_number) == len(number):
        answer += 1
    if answer == N:
        break
    i += 1

print(i)


## ---------------------------------------
# 백트랙킹을 활용한 풀이
import sys

sys.setrecursionlimit(10 ** 9)


def solve(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n >= 1023:  # 1022: 9876543210
        print(-1)  # N번째 감소하는 수 x
    elif n == 0:
        print(0)
    else:
        print(solve(n))
