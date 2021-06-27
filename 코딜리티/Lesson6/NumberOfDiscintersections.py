# distance 배열에 한 원의 최저점과 최고점을 담아 준다.
# 최저점인지, 최고점인지 구별하기 위해 튜플에 -1과 1을 같이 append 해준다.
# distance를 for문으로 순회하면서 answer에 중첩해서 쌓고, t에 현재 겹쳐진 distance의 갯수를 체크한다.

def solution(A):
    distance = []
    for i, v in enumerate(A):
        distance.append((i-v, -1))
        distance.append((i+v, 1))

    distance.sort()

    answer = 0 # 몇개가 포함되는지 반환
    t = 0 # 원이 시작 됐는데 아직 닫혀지지 않는 원의 개수

    for d in distance:
        if d[1] == 1:
            t -= 1 # 원이 닫힙
        else:
            answer += t
            t += 1 # 또 하나의 원이 열림

    if answer <= 10000000:
        return answer
    else:
        return -1
