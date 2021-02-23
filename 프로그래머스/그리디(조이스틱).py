def solution(name):
    # 각 알파벳에 대해서 최소 이동값을 구한다. 위로 움직여야 최소인지, 아래로 움직여야 최소인지를 구한다. A일 경우 리스트에 0이 들어간다.
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0

    while True:
        answer += make_name[idx]
        make_name[idx] = 0 #문자열을 맞춰줬기 때문에 0으로 바꿔준다.
        #값이 0이면 알파벳을 바꿀 필요가 없다. 모든 리스트의 값이 0이 될때까지 반복한다.
        if sum(make_name) == 0:
            break

        #좌우로 이동 방향을 정해 바꿔야하는 알파벳이 나오기까지 가장 짧은 거리를 구한다.
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1

        #해당 방향으로 위치를 조절한다.
        if left < right:
            answer += left
        else:
            answer += right

        if left < right:
            idx += -left
        else:
            idx += right

    return answer