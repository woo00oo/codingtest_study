# 첫번째 풀이 : 메모리 초과로 인한 실패 = 순열 사용

from itertools import permutations

L, C = map(int, input().split())
text = list(input().split())
pw_li = list(permutations(text, L))
pw_li.sort()
collection = {'a', 'e', 'i', 'o', 'u'}

for i in range(len(pw_li)):
    pw = list(pw_li[i])
    sort_pw = sorted(pw)

    # 오름차순
    if pw == sort_pw:
        collection_cnt, consonant_cnt = 0, 0
        for idx in range(len(pw)):
            if pw[idx] in collection:
                collection_cnt += 1
            else:
                consonant_cnt += 1

        # 최소 한개의 모음, 2개의 자음
        if collection_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(pw))

# 2번째 풀이 : 순열이 아니라 조합을 사용하여야 함.
# 순열로 경우의 수를 키울 필요없이(메모리초과) 오름차순으로 정렬 후에 조합을 사용
# 오름차순이 된 리스트를 조합할 경우 각 원소도 오름차순!!

from itertools import combinations

collection = {'a', 'e', 'i', 'o', 'u'}
L, C = map(int, input().split())
text = sorted(list(input().split()))
pw_li = list(combinations(text, L))

for i in range(len(pw_li)):
    pw = list(pw_li[i])
    collection_cnt, consonant_cnt = 0, 0
    for idx in range(len(pw)):
        if pw[idx] in collection:
            collection_cnt += 1
        else:
            consonant_cnt += 1

    # 최소 한개의 모음, 2개의 자음
    if collection_cnt >= 1 and consonant_cnt >= 2:
        print(''.join(pw))
