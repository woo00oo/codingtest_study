# 첫번째 시도 : BFS 활용 -> 성공

from collections import deque


def BFS(start_node, end_node):
    queue = deque()
    visited = [-1] * (N + 1)
    queue.append(start_node)

    while queue:
        node = queue.popleft()

        if node == end_node:
            return True

        if visited[node] == -1:
            queue.extend(myMap[node])
            visited[node] = 0

    return False


N = int(input())
M = int(input())
myMap = dict()
for i in range(1, N+1):
    myMap[i] = []
for i in range(1, N+1):
    li = list(map(int, input().split()))
    for idx, link in enumerate(li):
        if link == 1:
            myMap[i].append(idx+1)

plan = list(map(int, input().split()))

for i in range(M-1):
    check = BFS(plan[i], plan[i+1])
    if not check:
        print("NO")
        exit(0)

print("YES")


# ------------------------------------
# BFS나 DFS로도 해결이 가능하지만 경로의 거리에 대해 제한이 없고,
# 도착만 하면 되기 때문에 루트 노드를 확인해서 같은 집합에 있는지만 확인하는 유니온 파인드를 사용하여 간단하게 풀이.


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(a): # a 노드의 부모 노드 찾기
    if a == parent[a]: # a 노드가 부모 노드이면 a 반환
        return a
    p = find(parent[a]) # a 노드를 따라가면서 부모 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return p


def union(a, b): # a집합과 b집합 합치기
    a = find(a) # a 노드의 부모 노드 찾기
    b = find(b) # b 노드의 부모 찾기

    if a == b: # 이미 동일한 집합이면 연결시에 순환이 발생
        return

    if a < b: # a의 부모가 b 부모보다 상위 루트이면
        parent[b] = a # b의 부모를 a의 부모로 변경
    else: # b의 부모가 a 부모보다 상위 루트이면
        parent[a] = b # a의 부모 변경

N = int(input()) # 노드 수 입력 받기
M = int(input()) # 정점 수 입력 받기
parent = [0] * (N+1) # 부모 테이블 초기화

# 부모 테이블 상에서 자기 자신을 부모로 설정
for i in range(1, N+1):
    parent[i] = i

for x in range(1, N+1): # y번째 도시
    maps = list(map(int, input().split())) # y번째 도시가 어느 도시와 연결되어 있는지 정보
    for y in range(1, len(maps)+1): # y도시 연결 정보 추출
        if maps[y-1] == 1: # x 도시와 연결되어 있으면
            union(x, y) # 두 도시를 결합

tour = list(map(int, input().split())) # 여행 계획 정보
result = set([find(i) for i in tour]) # 여행 계획의 루트 노드 찾기
if len(result) != 1: # set 개수가 2개 이상이면 두개의 집합이 존재
    print('NO')
else:
    print('YES') # set 개수가 1이면 한 개의 집합이 존재


