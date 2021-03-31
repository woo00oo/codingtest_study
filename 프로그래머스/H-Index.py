# 문제를 이해하는 데 시간이 오래 걸렸다.
# h가 발표한 논문의 인용 횟수와 다르다는 것을 주의!

def solution(citations):
    citations.sort()
    answer = 0

    for i in range(len(citations)):
        if len(citations[i:]) >= citations[i]:
            answer = citations[i]

    return answer


def solution2(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0