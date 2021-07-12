maxL = 0
maxH = 0
maxIndex = 0
pillar = []
N = int(input())

# 가장 큰 높이값과 그 높이값의 index, 가장 긴 L 찾기
for _ in range(N):
    L, H = map(int, input().split())
    pillar.append((L, H))

    if maxL < L:
        maxL = L

    if maxH < H:
        maxH = H
        maxIndex = L

pillar_li = [0] * (maxL + 1)
for l, h in pillar:
    pillar_li[l] = h

answer = 0
temp = 0
# 왼쪽 (0 ~ 가장 큰 높이값)
for i in range(maxIndex + 1):
    if pillar_li[i] > temp:
        temp = pillar_li[i]
    answer += temp

temp = 0
# 오른쪽(마지막기둥 위치 ~ 가장 큰 높이값)
for i in range(maxL, maxIndex, - 1):
    if pillar_li[i] > temp:
        temp = pillar_li[i]
    answer += temp

print(answer)


