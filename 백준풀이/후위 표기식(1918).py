# 스택 자료구조 활용

operation = input()
stack = []
answer = ''

for op in operation:
    if op.isalpha():
        answer += op
    else:
        if op == '(':
            stack.append(op)
        elif op == '*' or op == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(op)
        elif op == '+' or op == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(op)
        elif op == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            # '(' 제거
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)