# 편의점과 도착지 좌표를 distance에 저장

from collections import deque
import sys

input = sys.stdin.readline

def BFS(x, y):
    queue, visited = deque(), []
    queue.append((x, y))
    visited.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            print("happy")
            return
        for nx, ny in distance:
            if (nx, ny) not in visited:
                dis = abs(nx - x) + abs(ny - y)
                if 20*50 >= dis:
                    queue.append((nx, ny))
                    visited.append((nx, ny))
    print("sad")
    return

T = int(input())
while T:
    n = int(input())
    start_x, start_y = map(int, input().split())
    distance = []
    for _ in range(n):
        x, y = map(int, input().split())
        distance.append([x, y])
    end_x, end_y = map(int, input().split())
    distance.append([end_x, end_y])
    BFS(start_x, start_y)
    T -= 1