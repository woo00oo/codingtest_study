#문제풀이 : 스택 자료 구조를 활용한 풀이
#   맨처음 스택에 number의 가장 첫번째 숫자를 넣어준다.
#   반복문을 돌아 스택 맨위의 수(stack[-1]) 가 num보다 작으면 스택에서 pop()을 해준다.
#   크기순으로 정렬이 되어있어 k개 만큼 빼지 못할 경우 stack[:-k]로 처리해준다.

def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)