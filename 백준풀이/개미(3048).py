# 첫번째 풀이 : 실패
# 이유 -> 이미 원하는 방향으로 이동한 개미를 또 다시 체인지 시켜줘 반대 방향으로 이동 시킴

# N1, N2 = map(int,input().split())
# group1 = list(input())
# group1.reverse()
# group2 = list(input())
# T = int(input())
# g = dict()
# for ant in group1:
#     g[ant] = 'R'
# for ant in group2:
#     g[ant] = 'L'
# time = 0
# change = 1
# answer = group1 + group2
# while True:
#     cnt = change
#     if time == T:
#         answer = ''.join(answer)
#         print(answer)
#         break
#
#     for i in range(1, len(answer)):
#         if cnt == 0:
#             break
#         if g[answer[i]] != g[answer[i-1]]:
#             answer[i], answer[i-1] = answer[i-1], answer[i]
#             cnt -= 1
#
#     change += 1
#     time += 1

## 2번째 풀이
N1, N2 = map(int,input().split())
group1 = input()
group2 = input()
T = int(input())
answer = group1[::-1] + group2

if T == 0:
    print(answer)
else:
    for _ in range(T):
        idx_arr = []
        for idx in range(1, len(answer)):
            if answer[idx-1] in group1 and answer[idx] in group2:
                idx_arr.append(idx)

        for i in idx_arr:
            answer = answer[:i-1] + answer[i] + answer[i-1] + answer[i+1:]

    print(answer)