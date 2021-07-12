# 1차 시도 : 실패
# 이유: numbers의 길이가 0이 될때 까지 순서에 맞지 않으면 모두 추가 해줌.
# ex) 1 3 2 4 5 6의 경우 실패

from collections import deque

N = int(input())
numbers = deque(list(map(int, input().split())))
stack = []
cnt = 1

while numbers:
    num = numbers.popleft()
    if cnt == num:
        cnt += 1
    else:
        stack.append(num)

check = True
for i in range(len(stack)-1, -1, -1):
    if cnt != stack[i]:
        check = False
        break
    cnt += 1

if check:
    print("Nice")
else:
    print("Sad")

# 2차 시도:
# 큐가 없을 때 까지 반복 -> 큐의 맨 처음 값이 i가 아니라면 스택에 추가 -> 스택의 맨 마지막 값이 i가 아닐 때까지 pop -> 마지막에 스택이 남아있는지 확인

from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
stack = deque()
i = 1
while queue:

    if queue and queue[0] == i:
        queue.popleft()
        i += 1
    else:
        stack.append(queue.popleft())

    while stack and stack[-1] == i:
        stack.pop()
        i += 1

print("Nice" if not stack else "Sad")