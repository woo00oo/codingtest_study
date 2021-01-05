N = int(input())
score_list = [0]
for _ in range(N):
    score_list.append(int(input()))

level = N
count = 0
while level != 1:
    if score_list[level] > score_list[level-1]:
        level -= 1
    else:
        score_list[level-1] -= 1
        count += 1
print(count)
