import sys
sys.setrecursionlimit(1000000)

result = 0
def treeInorderTraversal(num, a, graph, visited):
    global result

    visited[num] = True

    for node in graph[num]:
        if not visited[node]:
            a[num] += treeInorderTraversal(node, a, graph, visited)

    result += abs(a[num])

    return a[num]

def solution(a, edges):
    sumWeight = 0
    isZeroTrue = True

    for weight in a:
        sumWeight += weight
        if weight != 0:
            isZeroTrue = False

    if sumWeight != 0:
        return -1
    elif isZeroTrue:
        return 0
    else:
        graph = dict()
        for i in range(len(a)):
            graph[i] = []

        visited = [False] * len(a)

        for edge in edges:
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)

        treeInorderTraversal(0, a, graph, visited)
        return result