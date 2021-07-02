# 첫번째 풀이 시간 초과
# 이유 자기가 포함된 집합을 찾는 n만큼 반복문을 수행하기 때문.
#
import sys

n, m = map(int, input().split())
set_list = [{i} for i in range(n+1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    a_idx, b_idx = 0, 0
    if c == 0:
        for i in range(len(set_list)):
            if a in set_list[i]:
                a = set_list[i]
                a_idx = i
            if b in set_list[i]:
                b = set_list[i]
                b_idx = i

        sum_set = a | b
        if a != b:
            del set_list[a_idx]
            del set_list[b_idx-1]
        else:
            del set_list[a_idx]

        set_list.append(sum_set)
    else:
        check = False
        for S in set_list:
            if a in S and b in S:
                print('YES')
                check = True
                break
        if not check:
            print('NO')

#---------------------

# 두번째 풀이
# 집합 n+1개를 만들고 자기자신을 부모로 설정

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())

parent = [0] * (N+1) # 부모 테이블 생성
for i in range(N+1): # 자기 자신을 부모로 설정
    parent[i] = i

# 루트 노드 찾는 함수
def find(a):
    if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
        return a
    p = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a,b):
    a = find(a) # a의 루트 노드 찾기
    b = find(b) # b의 루트 노드 찾기

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    o, a, b = map(int,input().split()) # operation, 원소, 원소
    if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
        union(a,b)
    elif o == 1: # 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
