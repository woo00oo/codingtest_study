N = int(input())
parents = list(map(int,input().split()))
del_node = int(input())
tree = dict()
for i in range(N):
    if i == del_node or parents[i] == del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i]

answer = 0
if -1 in tree:
    stack = [-1]
else:
    stack = []
while stack:
    node = stack.pop()
    if node not in tree:
        answer += 1
    else:
        stack += tree[node]
print(answer)
