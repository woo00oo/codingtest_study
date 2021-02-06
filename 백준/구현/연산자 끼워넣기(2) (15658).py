from collections import deque
n = int(input())
li = list(map(int,input().split()))
oper = list(map(int,input().split()))

q = deque()
q.append([li[0],oper])

case = len(q)

for i in range(1,n):
    # q에 들어간 만큼 진행.
    for _ in range(case):
        x, y = q.popleft()

        # 덧셈
        if y[0] > 0:
            q.append([x+li[i],[y[0]-1,y[1],y[2],y[3]]])
        # 뺄셈
        if y[1] > 0:
            q.append([x-li[i],[y[0],y[1]-1,y[2],y[3]]])
        # 곱셈
        if y[2] > 0:
            q.append([x*li[i],[y[0],y[1],y[2]-1,y[3]]])
        # 나눗셈
        if y[3] > 0:
            if x < 0:
                q.append([-(-(x)//li[i]),[y[0],y[1],y[2],y[3]-1]])
            else:
                q.append([(x//li[i]),[y[0],y[1],y[2],y[3]-1]])

    case = len(q)

print(max(q)[0])
print(min(q)[0])