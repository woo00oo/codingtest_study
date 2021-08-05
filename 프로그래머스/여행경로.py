# 1차 풀이 : BFS 활용 실패

from collections import deque


def BFS(graph, start_node):
    visited = []
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()

        if node not in visited:
            if node in graph:
                queue.extend(graph[node])
            visited.append(node)

    return visited


def solution(tickets):
    graph = dict()
    for i in range(len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        if start in graph:
            graph[start].append(end)
            graph[start].sort()
        else:
            graph[start] = [end]
    print(graph)
    answer = BFS(graph, "ICN")

    return answer

'''
2차 풀이 : DFS 활용

graph라는 딕셔너리를 만들어주는 것은 위의 풀이와 동일하다.
하지만 value 부분을 오름차순이 아닌 내림차순으로 정렬한다. => 스택을 사용하기 때문에 내림차순으로 정렬해 사전순으로 도착지를 설정.

ICN 부터 visited에 넣어주고,

가장 최근에 추가된 출발지 = 현재 출발지(current)에서 갈 수 있는 도착지가 존재할 경우 갈 수 있는 도착지들 중 알파벳이 앞선 도착지를 꺼내 visited에 넣어준다

도착지가 존재하지 않을 경우 answer에 현재 출발지를 pop해서 넣어준다.



'''


def solution(tickets):
    answer = []
    graph = dict()
    for i in range(len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        if start in graph:
            graph[start].append(end)
            graph[start].sort(reverse=True)
        else:
            graph[start] = [end]

    visited = ["ICN"]

    while visited:
        current = visited[-1]
        if current in graph and graph[current]:
            visited.append(graph[current].pop())
        else:
            answer.append(visited.pop())

    answer.reverse()
    return answer