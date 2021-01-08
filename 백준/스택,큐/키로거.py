#문제 풀이 :
    #스택 두 개 활용, 스택 두개의 중간 지점을 커서로 간주.
    #문자 입력 : 왼쪽 스택에 원소를 삽입.
    #-입력 : 왼쪽 스택에서 원소를 삭제.
    #<입력:왼쪽스택에서 오른쪽스택으로 원소를 이동.
    #<입력:오른쪽스택에서 왼쪽 스택으로 원소를 이동
    #마지막에 출력시 오른쪽 스택은 뒤집어서 왼쪽 +오른쪽(reversed) 로 출력.



test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
