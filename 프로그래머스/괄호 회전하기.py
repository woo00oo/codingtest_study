# 내 풀이 :
#   o(n^2)이라 시간초과가 뜰 줄 알았는데 통과.
#   두번째 반복문 에서 조건에 맞지 않은 경우에는 break을 하기 때문에 시간초과가 뜨지 않았던 거 같다.

from collections import deque

def solution(s):
    queue = deque(s)
    dic = {'{': '}', '[': ']', '(': ')'}
    answer = 0

    for i in range(len(s)):
        if i != 0:
            queue.rotate(1)
        stack = []
        check = True
        for j in range(len(queue)):
            if queue[j] in ('[', '(', '{'):
                stack.append(queue[j])
            else:
                if stack:
                    if dic[stack[-1]] == queue[j]:
                        stack.pop()
                    else:
                        check = False
                        break
                else:
                    check = False
                    break

        if check and not stack:
            answer += 1

    return answer

# 다른 사람 풀이:
# 다른 사람도 똑같이 O(n^2)으로 풀이

def solution(s):
    answer = 0
    dic = {'{': '}', '[': ']', '(': ')'}

    for i in range(len(s)):
        right = list(s[i:] + s[:i])
        left = []

        while right:
            temp = right.pop(0)
            if not left:
                left.append(temp)
            else:
                if left[-1] in ['}', ')', ']']:
                    break

                if dic[left[-1]] == temp:
                    left.pop()
                else:
                    left.append(temp)

        if not left:
            answer += 1

    return answer