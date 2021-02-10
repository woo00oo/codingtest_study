# 숫자의 각 자리수는 문자열 -> list로 변환후 인덱스로 접근.
# 순열 라이브러리 사용

import sys
from itertools import permutations

n = [1,2,3,4,5,6,7,8,9]
num = list(permutations(n,3))

t = int(sys.stdin.readline())
for _ in range(t):
    test, s, b = map(int,sys.stdin.readline().split())
    test = list(str(test))
    removed_cnt = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= removed_cnt #리스트에서 제거된 튜플(리스트의 각 원소)의 개수

        for j in range(3):
            test[j] = int(test[j])
            if j == num[i].index(test[j]):
                s_cnt += 1
            else:
                b_cnt += 1

        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            removed_cnt += 1

print(len(num))