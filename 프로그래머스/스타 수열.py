# 스타 수열을 생성하기 위해서는 반드시 핵심 공통값이 있어야 한다.
# Counter 라이브러리를 활용하여 공통 원소의 개수가 몇 개로 구성되어 있는지 찾는다.

from collections import Counter


def solution(a):
    answer = -1
    if len(a) == 1:
        return 0

    c = Counter(a)

    for k, v in c.items():
        # k의 값을 기준으로 스타수열을 만드는데
        # 2배가 최대의 max길이 배열인데 answer보다 작다면 진행할필요 x(시간초과 방지)
        if v * 2 < answer:
            continue

        idx = 0
        common_value = k
        length = 0
        while idx < len(a) - 1:
            # idx랑 idx+1의 max_value의 값이 없으면 진행x
            # 둘의 값이 같다면 진행x
            if (a[idx] != common_value and a[idx + 1] != common_value) or a[idx] == a[idx + 1]:
                idx += 1
                continue

            # max_value를 포함하고 둘의 값이 같지 않다면
            # 조건을 만족하기 때문에 길이랑 idx랑 2씩 증가후 다음 배열 탐색
            length += 2
            idx += 2

        answer = max(answer, length)

    return answer