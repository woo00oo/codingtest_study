#문제해결 :
#   DFS= 스택으로 구현(작은걸 먼저 방문하도록 정렬함)
#   BFS= 큐로 구현
#   모든 정점이 연결되어있는 연결그래프가 아닐수도 있다. (비연결 그래프시 예외처리 해야함)

N, M, V = list(map(int,input().split()))
graph = dict()
for _ in range(M):
    a,b = map(int,input().split())
    if a in graph:
        graph[a] = sorted(graph[a] + [b])
    else:
        graph[a] = [b]
    if b in graph:
        graph[b] = sorted(graph[b] + [a])
    else:
        graph[b] = [a]


def DFS(graph, V):
    visited = list()
    need_list = list()

    need_list.append(V)

    while need_list:
        node = need_list.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            if node not in graph:
                break

            dfs_arr = sorted(graph[node],reverse=True)
            need_list.extend(dfs_arr)


def BFS(graph, V):
    visited = list()
    need_List = list()

    need_List.append(V)

    while need_List:
        node = need_List.pop(0)
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            if node not in graph:
                break
            need_List.extend(graph[node])


DFS(graph, V)
print()
BFS(graph, V)
