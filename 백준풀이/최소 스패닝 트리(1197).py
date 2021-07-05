# 부모 노드를 확인하여 부모 노드가 같다면 싸이클 발생

from sys import stdin

read = stdin.readline
V, S = map(int, read().split())

edge = []
for _ in range(S):
    a, b, weight = map(int, read().split())
    edge.append((weight, a, b))

# 간선 가중치가 작은 순으로 정렬
edge.sort(key=lambda x: x[0])

# 각 노드의 부모 노드를 자기 자신으로 설정
parent = [i for i in range(V+1)]


def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)

    if node2 < node1:
        parent[node1] = node2
    else:
        parent[node2] = node1

def find(node):
    if node == parent[node]: # 자기 자신이 루트 노드이면 node 반환
        return node
    parent[node] = find(parent[node])
    return parent[node]


sum = 0
for weight, start, end in edge:
    if find(start) != find(end):
        union(start, end)
        sum += weight

print(sum)