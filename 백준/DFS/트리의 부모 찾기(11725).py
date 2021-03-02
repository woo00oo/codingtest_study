#파이썬 제출 : 시간초과
#pypy 제출 : 런타임 에러 발생
# DFS 시작 방법이 잘못되었다. 루트노드 1부터 DFS를 실시하여 각 노드의 부모 노드를 하나의 리스트에다가 저장시켜 마지막에 하나씩 출력해주면 된다.
# 부모 노드는 이전 노드에 방문한 노드가 부모노드가 된다.

# import sys
# sys.setrecursionlimit(10 ** 9)
# def DFS(node, root):
#     if node == '1':
#         print(root[1])
#         return
#     li = Tree[node]
#     for index in li:
#         if index not in root:
#             root.append(index)
#             DFS(index, root)
#         else:
#             return
#
#
#
# N = int(input())
# Tree = dict()
# for i in range(1, N + 1):
#     Tree[str(i)] = list()
# for _ in range(N - 1):
#     x, y = map(str, sys.stdin.readline().split())
#     Tree[x].append(y)
#     Tree[y].append(x)
#
# for i in range(2, N+1):
#     li = [i]
#     DFS(str(i), li)



import sys

node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

# 트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)


# DFS나 BFS나 무관

def dfs(graph_list, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent


for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])
