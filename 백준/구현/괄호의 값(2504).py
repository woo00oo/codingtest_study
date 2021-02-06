#문제풀이 :
#   괄호 문제는 스택 자료구조를 적극 활용하자.

String = input()
stack = list()
answer = 0

for word in String:
    if word == ')':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2 * t)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    elif word == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        stack.append(word)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        answer += i
print(answer)