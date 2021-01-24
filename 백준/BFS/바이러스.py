#문제해결:
#   1번 노드로 부터 BFS를 활용해 방문한 노드가 총 몇개인지를 구하면 정답.

N = int(input())
V = int(input())
graph = dict()
for i in range(1,N+1):
    graph[i] = []
for _ in range(V):
    link = list(map(int,input().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

def BFS(graph):
    visited = list()
    need_visit = list()
    need_visit.append(1)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])


    return len(visited) - 1

print(BFS(graph))