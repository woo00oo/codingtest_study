def solution(n, results):
    # wins[key] = key가 이긴 사람들의 집합
    # loses[key] = key가 이기지 못한 사람들의 집합
    wins, loses = {}, {}
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n + 1):
        for battle in results:
            if battle[0] == i:  # i의 승리. i가 이긴 사람들
                wins[i].add(battle[1])
            if battle[1] == i:  # i의 패배. i가 진 사람들
                loses[i].add(battle[0])
        # i를 이긴 사람들 (loses[i]) => i에게 진 사람(wins[i])은 반드시 이긴다
        for winner in loses[i]:
            wins[winner].update(wins[i])
        # i에게 진 사람들 (wins[i]) => i를 이긴 사람들(loses[i])에게는 반드시 진다
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1

    return cnt

'''
문제 풀이 :
    처음 접해보는 유형이라 문제를 어떤식으로 풀어 나가야 할지 감이 오지 않아 구글링을 통해 해결.
    
    문제의 핵심은 다음 2가지 이다
    
    1) 선수 A가 있을때 A를 이긴 사람과 A에게 진사람의 수를 합치면 n-1이 되도록 만드는 것
    
    2) A에게 진 사람은 A를 이긴 사람에게 반드시 진다 => A를 이긴 사람은 A에게 진 사람을 반드시 이긴다 라는 조건



'''