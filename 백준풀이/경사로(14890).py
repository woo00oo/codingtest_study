'''
check함수는 리스트를 받아서 지나갈 수 있는 길인지 검사해주는 함수이다.

리스트를 앞에서부터 차례대로 검사한다.

만약 앞 뒤 차이가 2 이상 난다면 그건 지나갈 수 없는 길이다.

그리고 길이가 같다면 패스한다.

차이가 1 난다면 경사로를 놓아주는데 이미 경사로가 놓아져 있거나 경사로를 놓을 수 없으면 False를 리턴한다.
'''


import sys


input = sys.stdin.readline


def check(li):
    sw = [False for _ in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue
        if abs(li[i] - li[i + 1]) > 1:
            return False
        if li[i] > li[i + 1]:
            temp = li[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False
                    if sw[j]:
                        return False
                    sw[j] = True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False
                    if sw[j]:
                        return False
                    sw[j] = True
                else:
                    return False
    return True


n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
for i in s:
    if check(i):
        cnt += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(s[j][i])
    if check(temp):
        cnt += 1
print(cnt)