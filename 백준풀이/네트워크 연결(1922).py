# 최소 스패닝 트리 활용

def find(a):
    if a == parent[a]:
        return a

    p = find(parent[a])
    parent[a] = p
    return parent[a]

def uion(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

N = int(input())
M = int(input())
trunk = []
answer = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    trunk.append((a, b, c))

trunk.sort(key=lambda x: x[2], reverse=True)

trunk_len = 0
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i

while True:
    if trunk_len == N-1:
        break

    a, b, c = trunk.pop()

    check = uion(a, b)

    if check:
        answer += c
        trunk_len += 1

print(answer)
