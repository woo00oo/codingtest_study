#문제풀이 : brown과 yellow를 더한다 ( 전체 카펫의 칸)
#   for문을 통해 가로를 확인. i로 나눠지면 i가 가로, a는 세로


def solution(brown, yellow):
    area = brown + yellow
    for width in range(area,2,-1):
        if area % width == 0:
            height = area // width
            if yellow == (width-2)*(height-2):
                return [width, height]