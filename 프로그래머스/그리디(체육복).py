def solution(n, lost, reserve):
    li = [i for i in range(1,n+1)]
    answer = 0
    for student in li:
        if student in lost:
            if student in reserve:
                answer += 1
                reserve.remove(student)
            elif student-1 in reserve:
                if student-1 not in lost:
                    answer += 1
                    reserve.remove(student-1)
            elif student+1 in reserve:
                if student+1 not in lost:
                    answer += 1
                    reserve.remove(student+1)
        else:
            answer += 1
    return answer