from math import ceil


def solution(progresses, speeds):
    answer = []
    reminder = []

    for i in range(len(progresses)):
        work = 100 - progresses[i]
        reminder.append(ceil(work/speeds[i]))

    stack = [reminder[0]]

    for i in range(1, len(reminder)):
        if max(stack) >= reminder[i]:
            stack.append(reminder[i])
        else:
            answer.append(len(stack))
            stack = [reminder[i]]

    answer.append(len(stack))

    return answer