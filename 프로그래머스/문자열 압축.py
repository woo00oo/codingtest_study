def solution(s):
    answer = len(s)

    # 문자열을 2로 나누어 문자열 길이보다 더 넘어가는 비교는 할 필요가 없음( 절반보다 큰 문자열은 반복될수가 없음)
    for l in range(1,len(s) // 2 + 1):
        S = ''
        cnt = 1
        for i in range(0,len(s),l):
            # 반복 되면 반복되는 수를 1증가
            if s[i:i+l] == s[i+l:i+l+l]:
                cnt += 1
            # 반복 되지 않을 경우
            else:
                # 한번도 반복되지 않을 경우
                if cnt == 1:
                    # 그대로 문자열 뒤에 붙혀줌
                    S += s[i:i+l]
                # 여러번 반복 되어 있을 경우 반복된 횟수 + 반복된 문자열을 뒤에 붙혀줌
                else:
                    S += str(cnt) + s[i:i+l]
                # 반복된 횟수는 1로 초기화 시켜줌
                cnt = 1

        # 가장 작은 문자열의 길이(압축 크기가 가장 작음)를 저장
        if answer > len(S):
            answer = len(S)

    return answer


