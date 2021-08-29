'''
초당 처리량이 바뀌는 시점 = 어떤 요청이 시작하거나 끝나는 시점

응답 완료 시간(S)와 처리시간(T)를 이용하여 요청의 시작시간, 끝 시간을 구해 logs 배열에 추가 => (start_time, end_time)

해당 시점마다 초당 처리량을 계산해서 최댓값을 구해 반환.

시간은 모두 밀리초(msec)로 바꾼 후 풀이.


'''


def solution(lines):
    answer = 0
    logs = []

    for line in lines:
        date, S, T = line.split()
        S = S.split(':')
        T = T.replace('s', '')

        # 끝 시간을 msec 단위로 저장
        end_time = (int(S[0]) * 3600 + int(S[1]) * 60 + float(S[2])) * 1000
        # 시작 시간을 msec 단위로 저장(처리시간은 시작시간과 끝시간을 포함하기 때문에 +1)
        start_time = end_time - float(T) * 1000 + 1

        logs.append((start_time, end_time))

    for log in logs:
        answer = max(answer, throughput(logs, log[0], log[0] + 1000), throughput(logs, log[1], log[1] + 1000))

    return answer


def throughput(logs, start_time, end_time):
    cnt = 0

    for log in logs:
        # 요청의 시작 시간이 ent_time 보다 작고 끝 시간이 start_time 보다 클 경우.
        if log[0] < end_time and log[1] >= start_time:
            cnt += 1

    return cnt