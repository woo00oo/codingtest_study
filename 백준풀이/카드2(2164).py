# pop(0) 의 시간복잡도 -> O(N)
# popleft() 의 시간복잡도 -> O(1)


from collections import deque

# N = int(input())
# stack = [i for i in range(1, N + 1)]
#
# while stack:
#     if len(stack) == 1:
#         print(*stack)
#         exit(0)
#
#     # 맨위의 카드를 버린다.
#     stack.pop(0)
#
#     # 그 다음 맨 위에 있는 카드를 아래에 있는 카드 밑으로 옮긴다.
#     card = stack.pop(0)
#     stack.append(card)


N = int(input())
queue = deque([i for i in range(1, N+1)])

while queue:
    if len(queue) == 1:
        print(*queue)
        exit(0)

    queue.popleft()

    card = queue.popleft()
    queue.append(card)