# 문제해결:
#   거짓말을 하면 안 될 사람들을 찾아내고 그 사람들 전부가 속하지 않은 파티의 수를 알아내면 된다.
#   거짓말을 하면 안 될 사람들 = 진실을 알고 있는 사람 + 진실을 알고 있는 사람과 같은 파티에 참석하는 사람들

# 1. 거짓말을 하면 안 될 사람들이 담긴 스택에서 한 명을 pop한다.
# 2. pop된 사람이 포함된 파티들을 진실을 말해야하는 파티라고 표기해둔다.
# 3. 파티 목록을 탐색하여 pop한 사람과 같은 파티에 있는 사람들을 찾는다.(union)
# 4. 찾은 사람들을 거짓말을 하면 안 될 사람들이 담긴 스택에 추가한다.
#   스택에 추가된 적이 없는 사람만을 추가한다.
# 5. 스택이 빌때까지 이 과정을 반복한다.
# 6. 반복이 종료되면 표기되지 않은 파티의 개수를 세어 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 거짓말을 하면 안 될 사람들을 담는 스택
# 진실을 아는 사람의 수는 필요가 없어 슬라이싱 함
know = list(map(int, input().split()))[1:]

# 스택에 추가된 적이 있는지 확인하기 위한 리스트
visit = [0] * N
for k in know:
    visit[k-1] = 1

# 파티 손님의 수는 필요가 없어 슬라이싱 함
parties = [list(map(int, input().split()))[1:] for _ in range(M)]

party_visit = [0] * M  # 진실을 말해야 하는 파티일 경우 1이라고 표기

# 스택이 빌때까지 과정 반복
while know:
    known_guest = know.pop()

    candidate = set()  # pop된 사람들과 같은 파티에 있는 사람들을 담는 집합

    # pop된 사람과 같은 파티에 있는 사람들을 찾아 집합에 추가한다.
    for party_idx in range(len(parties)):
        party = set(parties[party_idx])
        if known_guest in party:  # pop된 사람이 현재 파티에 있을 경우
            candidate = candidate.union(party)  # 파티의 사람들을 집합에 추가
            party_visit[party_idx] = 1  # 현재 파티를 진실을 말해야 하는 파티라고 표기

    # 찾은 사람들 중 스택에 추가된 적이 없는 사람들을 스택에 추가
    for guest in candidate:
        if not visit[guest - 1]:
            know.append(guest)
            visit[guest - 1] = 1

# 표기되지 않은 파티의 개수를 출력
print(party_visit.count(0))
