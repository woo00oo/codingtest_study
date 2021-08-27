'''

1> 문자열 -> 피연산자(numbers), 연산자(op)로 나눈다
2> 연산자 우선순위를 정한다 -> 순열 사용
3> 연산자 우선순위대로 계산 -> 결과값을 answer에 저장(절댓값)
4> 가장 큰 값을 반환

'''


from itertools import permutations


def solution(expression):
    answer = []
    op = []
    expression_li = list(expression)
    for i in range(len(expression_li)):
        if not expression_li[i].isdigit():
            op.append(expression_li[i])
            expression_li[i] = ','

    expression = ''.join(expression_li)

    numbers = expression.split(',')
    set_op = set(op)
    permu_op = list(permutations(set_op, len(set_op)))

    for i in range(len(permu_op)):
        test_numbers = numbers.copy()
        test_op = op.copy()

        for j in range(len(permu_op[i])):
            removed = 0
            for idx in range(len(test_op)):
                idx -= removed

                if permu_op[i][j] == test_op[idx]:
                    if test_op[idx] == '*':
                        num = int(test_numbers[idx]) * int(test_numbers[idx+1])
                    elif test_op[idx] == '-':
                        num = int(test_numbers[idx]) - int(test_numbers[idx+1])
                    else:
                        num = int(test_numbers[idx]) + int(test_numbers[idx+1])

                    test_op.pop(idx)
                    test_numbers[idx] = num
                    test_numbers.pop(idx+1)
                    removed += 1

        answer.append(abs(test_numbers[0]))

    return max(answer)


