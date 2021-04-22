# deque.rotate(n) => 큐 안의 요소들을 n 만큼 회전 해주는 메소드 n이 양수면 오른쪽으로 회전, 음수면 왼쪽으로 회전
from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int,input().split())
velt = deque(map(int,input().split()))
ans = 1

#robot이 들어온 순서대로 현재 자신의 위치를 담고있는다
robot =deque([0] * n)

while True:
    #1
    velt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0 #내려가는 위치에 로봇 삭제
    #2
    for i in range(n-2,-1,-1): #로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
        if robot[i] != 0 and robot[i+1] == 0 and velt[i+1] >= 1:
            velt[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[n-1] = 0 #내려가는 위치에 로봇 삭제
    #3
    if robot[0] == 0 and velt[0] > 0:
        velt[0] -= 1
        robot[0] = 1
    #4
    cnt = 0
    for i in range(len(velt)):
        if velt[i] == 0 :
            cnt += 1

    if cnt >= k:
        print(ans)
        break

    ans += 1