from collections import deque


def BFS(graph, n):
    queue = deque()
    visited = [-1] * (n+1)
    visited[1] = 0
    queue.append(1)

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

    return visited


def solution(n, edge):
    graph = dict()
    for i in range(1, n+1):
        graph[i] = []
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    result = BFS(graph, n)
    max_distance = max(result)
    answer = result.count(max_distance)
    return answer

'''
풀이 과정.

1) BFS를 통해 1번 노드로 부터 각 노드까지의 거리를 구해준다.

2) max_distance에 가장 먼 노드의 거리를 저장한다.

3) result 배열안에 가장 먼 노드의 거리를 가지는 원소가 몇 개 인지 구한다 -> 문제에서 원하는 답 return


'''

