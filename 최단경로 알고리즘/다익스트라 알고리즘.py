import heapq

mygraph = {
    'A':{'B':8,'C':1,"D":2},
    'B':{},
    'C':{'B':5,"D":2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def dijkstra(graph,start):

    distances = {node: float('inf')for node in graph}  #거리저장 배열 (시작 노드를 제외한 모든 노드까지의 거리를 무한대로 초기화)
    distances[start] = 0
    print(distances)
    queue = [] #우선순위 큐
    heapq.heappush(queue,[distances[start],start])

    while queue: #우선순위 큐에 노드가 없을때 까지 반복
        current_distance,current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent,weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue,[distance,adjacent])

    return distances

print(dijkstra(mygraph,'A'))
print(mygraph['A'])