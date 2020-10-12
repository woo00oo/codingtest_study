graph = {
    'vertices':['A','B','C','D','E','F','G'], #노드
    'edges':[
        (7,'A','B'),(5,'A','D'),
        (7,'B','A'),(8,'B','C'),(9,'B','D'),(7,'B','E'),
        (8,'C','B'),(5,'C','E'),
        (5,'D','A'),(9,'D','B'),(7,'D','E'),(6,'D','F'),
        (7,'E','B'),(5,'E','C'),(7,'E','D'),(8,'E','F'),(9,'E','G'),
        (6,'F','D'),(8,'F','E'),(11,'F','G'),
        (9,'G','E'),(11,'G','F') #각 노드 기준으로 연결된 간선을 모두 작성
    ]
}

parent=dict() #부모노드의 값을 저장
rank=dict() #랭크의 값을 저장

def find(node):
    #path compression 기법
    if parent[node] != node : #부모 노드가 존재함
        parent[node] = find(parent[node])
    return parent[node]   #루트 노드를 리턴함
def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    #union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1



#그래프의 각 노드들을 원소 하나하나의 부분집합으로 분리하는 함수
def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    #1. 초기화
    for node in graph['vertices']:
        make_set(node)

    #2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    #3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u): #양 끝의 노드의 루트노드가 같은 지 비교(사이클이 있는지 확인)
            union(node_v,node_u)
            mst.append(edge)

    return mst #최소 신장 트리를 반환

print(kruskal(graph))