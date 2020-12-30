# Union-Find 알고리즘
#
# - Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활용하는 알고리즘
# - 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때(합칠 때)사용
# - Disjoint Set이란
#
#      - 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
#
#      - 공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
#
#      - Disjoint Set= 서로소 집합 자료구조
#
#   1. 초기화
#
#      n개의 원소가 개별 집합으로 이뤄지도록 초기화
#
#   2. Union
#
#      두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬
#
#    3. Find
#
#     여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소(즉, 루트노드)를 확인

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y :
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        #초기화
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
    union(x, y)
    print(number[find(x)])





