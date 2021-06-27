# H[i+1]이 H[i]가 보다 크다면 벽은 점점 높아진다 (새로운 블록이 생긴다.)

def solution(H):
    stack = []
    count = 0

    for h in H:

        while stack and stack[-1] > h:
            stack.pop()

        if not stack or stack[-1] < h:
            count += 1
            stack.append(h)

    return count