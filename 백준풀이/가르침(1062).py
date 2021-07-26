# 첫번째 풀이 : 실패
# 원인 : 단어마다 중복된 글자 위주로 가르치더라도 K가 부족하여 한 글자도 읽지 못하는 경우가 발생할 수 있음
# ex)
'''
    필수 글자를 제외하고,
    [hb, dcs, dco, dckj], k = 2일 경우
    내가 짠 로직으로 가르칠 글자를 정하면 단어마다 중복된 글자가 많은 d, c가 뽑히게 된다.
    하지만 d,c를 가르쳤다고 하더라도 최대 읽을 수 있는 글자는 0이 된다.
    hb를 가르치면 1글자라도 가르칠 수 있기 때문에 오답...

'''

import sys

N, K = map(int, input().split())
study_word_list = {'a', 'n', 't', 'i', 'c'}
word_list = []
char_list = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    word_list.append(s[4:-4])

K -= 5
if K < 0:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)

for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        char_list.append([word_list[i][j], 0])

word_list = list(map(set, word_list))

for i in range(len(char_list)):
    cnt = 0
    for word in word_list:
        if char_list[i][0] in word:
            cnt += 1
    char_list[i][1] = cnt

char_list.sort(key=lambda x: x[1], reverse=True)

for i in range(len(char_list)):
    if K != 0 and char_list[i][0] not in study_word_list:
        study_word_list.add(char_list[i][0])
        K -= 1
    if K == 0:
        break

answer = 0
for word in word_list:
    check = True
    for char in word:
        if char not in study_word_list:
            check = False
    if check:
        answer += 1

print(answer)

# ------------------------

# 두번째 풀이 : 비트 마스킹 활용

from itertools import combinations
n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)

# 세번째 풀이 : 조합 브루트 포스
def go(n, k, words, elms_cnt, start, cnt, rlt, ans):
    if cnt == k - 5:
        scr = 0
        for word in words:
            check = True
            for w in word:
                if w not in rlt:
                    check = False
                    break
            if check:
                scr += 1
        ans[0] = max(ans[0], scr)
        return
    for i in range(start, elms_cnt):
        if chr(ord('a') + i) in ['a', 'n', 't', 'i', 'c']:
            continue
        rlt.append(chr(ord('a') + i))
        go(n, k, words, elms_cnt, i + 1, cnt + 1, rlt, ans)
        rlt.pop()


def solution(n, k, words):
    elms_cnt = ord('z') - ord('a') + 1
    ans = [0]
    go(n, k, words, elms_cnt, 0, 0, ['a', 'n', 't', 'i', 'c'], ans)
    return ans[0]


N, K = map(int, input().split())
Words = [input()[4:-4] for _ in range(N)]
print(solution(N, K, Words))