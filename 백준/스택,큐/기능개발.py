# 문제풀이:
#   math.ceil(올림)을 활용하여 소요시간을 각각 구한다.
#   progresses의 각 소요시간을 확인하는데 front에 가장 오래걸린 소요 시간의 인덱스를 저장해줌. (front = 0 초기값)
#   초기값보다 소요기간이 큰 인덱스가 구해지면 front를 그 인덱스로 초기화 시키고, 현재 인덱스 - 프론트인덱스의 값을 answer에 append한다.
#   반복문이 끝나면 progress의 전체길이 - 현재 프론트 인덱스의 값을 구해서 answer에 append




import math

def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:
            answer.append(idx - front)
            front = idx
    answer.append(len(progresses) - front)

    return answer



