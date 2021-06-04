# 벨만포드 알고리즘 활용. ( 다익스트라 알고리즘은 간선의 비용이 음의 경우에는 사용할 수 없음)
# - 음수 가중치가 있는 그래프의 시작 정점에서 다른 정점까지의 최단 거리를 구할 수 있음
# - 음수 사이클 존재의 여부를 알 수 있다.

# 모든 지점을 시작 지점으로 둘 필요가 없이, 시작 지점은 아무곳이나 두고(1) 음의 사이클이 존재하는지만 판단하면 된다.
# distance[start] != INF 삭제 -> 시작 위치와 연결되어 있을 경우에만
# 시작 위치와 연결되지 않더라도 거리들이 갱신된다.

# 음수 사이클이 존재하는지 확인
def bellmanFord(start):
    distance = [int(1e9) for _ in range(N+1)]
    distance[start] = 0

    # 음의 사이클 판별을 위해 n번 반복
    for i in range(N):
        # 반복마다 모든 간선 확인
        for edge in edges:
            current = edge[0]
            next_node = edge[1]
            cost = edge[2]

            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if distance[next_node] > cost + distance[current]:
                distance[next_node] = cost + distance[current]
                # n번 돌렸을 경우 갱신이 가능한 경우 음의 싸이클 존재
                if i == N - 1:
                    return True

    return False

T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    # 도로 정보
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 웜홀 정보
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellmanFord(1):
        print('YES')
    else:
        print('NO')


