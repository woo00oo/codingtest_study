# import sys
#
# N = int(input())
# state = list(map(int,sys.stdin.readline().strip()))
# goal_state = list(map(int,sys.stdin.readline().strip()))
# state = list(map(bool,state))
# goal_state = list(map(bool,goal_state))
#
# count = 0
# for index in range(N-1, -1, -1):
#     if state[index] != goal_state[index]:
#         if index == 0:
#             state[index] = not state[index]
#             state[index+1] = not state[index+1]
#         elif index == N - 1:
#             state[index] = not state[index]
#             state[index-1] = not state[index-1]
#         else:
#             state[index-1] = not state[index-1]
#             state[index] = not state[index]
#             state[index + 1] = not state[index + 1]
#
#         count += 1
#         index = N - 1
#     if index == 0 and state != goal_state:
#         count = -1
#
# print(count)
# 문제 해결 :
#   0번째 스위치가 눌렸을 경우와 누르지 않았을 경우를 두 메소드로 두어서 가능할 경우 최소값이 정답.
#   i번째 스위치를 눌러야 하는 경우는 i-1번째의 전구가 state[i-1] != result[i-1] 일 경우 스위치를 누른다.
import sys

def zeroClick(state):
    count=1
    state[0]=int(not state[0])
    state[1] = int(not state[1])
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1
def zeroNoClick(state):
    count=0
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1

n = int(sys.stdin.readline().rstrip("\n"))
state = list(map(int,sys.stdin.readline().rstrip("\n")))
result = list(map(int,sys.stdin.readline().rstrip("\n")))
res1 = zeroClick(state[:])
res2 = zeroNoClick(state[:])
if(res1>=0 and res2>=0):
    print(min(res1,res2))
elif(res1>=0 and res2<0):
    print(res1)
elif(res1<0 and res2>=0):
    print(res2)
else:
    print(-1)