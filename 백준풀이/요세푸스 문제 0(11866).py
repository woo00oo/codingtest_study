# 첫번째 풀이 : 단순 배열 인덱싱을 활용하여 풀이.

N, K = map(int, input().split())

people = [i for i in range(1, N+1)]
answer = []
next = K - 1

while True:
    p = people[next]
    del people[next]
    answer.append(p)

    if len(people) == 0:
        break

    next += (K - 1)
    if next >= len(people):
        next %= len(people)

answer = list(map(str, answer))
answer[0] = '<' + answer[0]
answer[-1] = answer[-1] + '>'
print(', '.join(answer))

# -----------------------------------------------------------------

# 두번째 풀이 : 큐의 자료구조를 활용하여 풀이.
# K번째까지 요소를 없애고, 그 요소들을 뒤에 추가

from collections import deque

N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

print('<', end='')

while queue:
    # for i in range(K-1):
    #     queue.append(queue[0])
    #     queue.popleft()
    queue.rotate(-(K-1))
    print(queue.popleft(), end='')

    if queue:
        print(', ', end='')
print('>')
