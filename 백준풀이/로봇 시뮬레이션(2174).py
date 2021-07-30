# 출력조건을 잘 신경 쓰자.....

dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
direction = {"N": 0, "E": 1, "S": 2, "W": 3}

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = []
command = []
for _ in range(N):
    x, y, d = input().split()
    robots.append([int(x), int(y), direction[d]])
for _ in range(M):
    n, t, cnt = input().split()
    command.append((int(n), t, int(cnt)))

for n, t, cnt in command:
    for _ in range(cnt):
        if t == 'L':
            robots[n-1][2] = (robots[n-1][2] - 1) % 4
        elif t == 'R':
            robots[n-1][2] = (robots[n-1][2] + 1) % 4
        else:
            nx = robots[n-1][0] + dx[robots[n-1][2]]
            ny = robots[n-1][1] + dy[robots[n-1][2]]
            if not (1 <= nx <= A and 1 <= ny <= B):
                print("Robot " + str(n) + " crashes into the wall")
                exit(0)

            for i in range(N):
                if i + 1 == n:
                    continue

                if nx == robots[i][0] and ny == robots[i][1]:
                    print("Robot " + str(n) + " crashes into robot " + str(i+1))
                    exit(0)

            robots[n-1][0] = nx
            robots[n-1][1] = ny

print("OK")