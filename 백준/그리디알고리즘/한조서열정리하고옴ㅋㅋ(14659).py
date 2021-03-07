N = int(input())
height = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if height[i] > height[j]:
            cnt += 1
        else:
            break
    answer.append(cnt)

print(max(answer))
