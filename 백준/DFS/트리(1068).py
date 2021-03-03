#문제풀이:
#   각 노드의 부모를 parents에 저장한다.
#   삭제할 노드도 del_node에 저장하고 tree 맵을 만든다.
#   parents를 for문으로 돌면서 삭제할 노드이거나 삭제할 노드를 부모로 둔 노드를 제외하고 tree에 저장
#   삭제한 노드가 루트라면 빈 리스트를, 아니라면 [-1]를 stack 저장한다
#   tree를 돌면서 리프 노드의 개수를 센다

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = dict()
for i in range(N):
    if i == del_node or parents[i] == del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i]

res = 0
if -1 in tree:
    stack = [-1]
else:
    stack = []
while stack:
    node = stack.pop()
    if node not in tree:
        res += 1
    else:
        stack += tree[node]
print(res)