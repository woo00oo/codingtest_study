'''

1.  모든 시간을 '초' 단위로 환산

    초로 환산된 play_time의 size 만큼 모든 시간별 시청자 수를 저장 => all_time 각 1초당 시청자수 누적하여 기록.


2.  시작 시간 -> 시청자 수 +1 , 종료 시간 -> 시청자 수 -1
    all_time[i] = i 시각에 시청중인 사람의 수


3.  2번 과정에서 해둔 start, end 체크를 바탕으로 모든 구간에 시청자수를 기록. => 구간별 시청자수 기록
    all_time[i] = all_time[i] + all_time[i-1] = (i-1부터 i까지) 1초 동안의 시청자수

4.  모든 구간 시청자 누적 기록
    all_time[i] = all_time[i] + all_time[i-1] = 0부터 i초 까지의 누적 시청자 수, 모든 시청자 수를 누적해서 쌓아준다.

5. 누적된 시청자수를 바탕으로 가장 시청자수가 많은 구간 탐색 => 현재 i의 누적 시청자수에서 i - adv_time 의 누적 시청자수를 빼면 해당 구간의 시청자수 값을 얻을 수 있다.
    most_view = all_time[i] - all_time[i - adv_time]


'''


def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)
    all_time = [0 for _ in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

