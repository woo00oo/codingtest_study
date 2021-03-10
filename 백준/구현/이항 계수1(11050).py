from itertools import combinations

N, K = map(int,input().split())
li = [i for i in range(1,N+1)]
C = list(combinations(li,K))
print(len(C))