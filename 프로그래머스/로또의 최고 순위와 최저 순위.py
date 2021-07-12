def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    win_nums = set(win_nums)
    max_rank = 0
    min_rank = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_rank += 1

    zero_cnt = lottos.count(0)
    max_rank = min_rank + zero_cnt
    min_rank = min_rank

    if max_rank in rank:
        answer.append(rank[max_rank])
    else:
        answer.append(6)

    if min_rank in rank:
        answer.append(rank[min_rank])
    else:
        answer.append(6)

    return answer