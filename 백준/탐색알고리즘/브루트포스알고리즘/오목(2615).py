import sys

dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]
black = [];
white = []
for i in range(1, 20):
    board = list(map(int, input().split()))
    for j in range(len(board)):
        if board[j] == 1:
            black.append([i, j + 1])
        elif board[j] == 2:
            white.append([i, j + 1])
# black부터 찾아보자
for b1 in black:
    r, c = b1
    for d in range(4):
        check_r, check_c = r, c
        cnt = 1
        while 0 <= check_r <= 19 and 0 <= check_c <= 19:
            if [check_r + dx[d], check_c + dy[d]] in black:
                cnt += 1
                check_r += dx[d];
                check_c += dy[d]
            else:
                break
            if cnt >= 5:
                break
        if cnt == 5:
            if [check_r + dx[d], check_c + dy[d]] not in black:
                if 1 <= r - dx[d] <= 19 and 1 <= c - dy[d] <= 19:
                    if [r - dx[d], c - dy[d]] not in black:
                        if d != 2:
                            print(1)
                            print(r, c)
                            sys.exit()
                        else:
                            print(1)
                            print(check_r, check_c)
                            sys.exit()
                else:
                    if d != 2:
                        print(1);
                        print(r, c), sys.exit()
                    else:
                        print(1);
                        print(check_r, check_c), sys.exit()

# white를 찾아보자
for b1 in white:
    r, c = b1
    for d in range(4):
        check_r, check_c = r, c
        cnt = 1
        while 0 <= check_r <= 19 and 0 <= check_c <= 19:
            if [check_r + dx[d], check_c + dy[d]] in white:
                cnt += 1
                check_r += dx[d];
                check_c += dy[d]
            else:
                break
            if cnt >= 5:
                break
        if cnt == 5:
            if [check_r + dx[d], check_c + dy[d]] not in white:
                if 1 <= r - dx[d] <= 19 and 1 <= c - dy[d] <= 19:
                    if [r - dx[d], c - dy[d]] not in white:
                        if d != 2:
                            print(2)
                            print(r, c)
                            sys.exit()
                        else:
                            print(2);
                            print(check_r, check_c);
                            sys.exit()
                else:
                    if d != 2:
                        print(2);
                        print(r, c), sys.exit()
                    else:
                        print(2);
                        print(check_r, check_c);
                        sys.exit()

print(0)