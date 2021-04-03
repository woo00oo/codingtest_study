# 문제해결:
#   좌표에서 방문 가능한 좌표로 이동한다면, 간선을 set에 저장해둔다.
#   (출발지점x, 출발지점y, 도착지점x, 도착지점y)
#   (도착지점x, 도착지점y, 출발지점x, 출발지점y)
#   겹치는 길이 있을 수 있으므로 set을 사용하고 len을 리턴
#   출발지점과 도착지점이 반대여도 같은 간선이기 때문에 한번 저장할때 두 튜플로 저장한다
#   두 튜플로 저장했기 때문에 len을 리턴할 때 => len // 2 처리


def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    road = set()
    cur_x, cur_y = (0, 0)

    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2