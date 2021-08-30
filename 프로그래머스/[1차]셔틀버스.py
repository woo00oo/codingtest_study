# 1차 풀이 : 정확도 70퍼

def solution(n, t, m, timetable):
    answer = ''
    bus_time = 9 * 60

    for i in range(len(timetable)):
        hh, mm = map(int, timetable[i].split(':'))
        timetable[i] = hh * 60 + mm

    timetable.sort()

    for number in range(n):
        if number == n-1:
            if len(timetable) >= m:
                max_time = max(timetable)
                if max_time > bus_time:
                    max_time = bus_time
                else:
                    max_time -= 1
            else:
                max_time = bus_time

            answer_h = str(max_time // 60)
            answer_m = str(max_time % 60)

            if len(answer_h) == 1:
                answer_h = '0'+answer_h

            if len(answer_m) == 1:
                answer_m = '0'+answer_m

            answer += answer_h + ":" + answer_m
        else:
            cnt = 0
            removed = []
            for i in range(len(timetable)):
                if bus_time >= timetable[i] and cnt < m:
                    removed.append(i)
                    cnt += 1
                else:
                    break

            for i in range(len(removed)):
                del timetable[removed[i]]

            bus_time += t

    return answer


# ---
# 다른 사람풀이
'''
시, 분 -> 분 단위로 모두 변환 
모든 크루원을 한 명씩 버스에 태움
한 명씩 버스에 태우다보면, 마지막 버스에 마지막 사람이 언제 탔는지를 알 수 있는데 그 값의 -1을 한 시간을 문자열로 반환.
만약 마지막에 버스에 전부 타지 않았다면, 마지막 버스 시간을 리턴.

'''


def solution(n, t, m, timetable):
    answer = ''
    crew = [int(tt.split(":")[0])*60+int(tt.split(":")[1]) for tt in timetable]
    # 크루의 도착시간
    crew.sort()

    # bus[x] = (버스시간, 승객 수, 마지막 탄 크루의 도착시간)
    bus = [(540+t*i, 0, None) for i in range(n)]

    bidx, cidx = 0, 0
    while cidx < len(crew):
        c = crew[cidx]
        if bidx == len(bus):
            break
        if c <= bus[bidx][0] and bus[bidx][1] < m:
            tt, cnt, _ = bus[bidx]
            bus[bidx] = (tt, cnt+1, c)
            cidx += 1
        else:
            bidx += 1

    ret = bus[-1][0]
    if bus[-1][2]:
        if bus[-1][1] == m:
            ret = bus[-1][2] - 1

    return '%02d:%02d' % (ret // 60, ret % 60)
