def solution(genres, plays):
    total_plays = dict()
    play_list = dict()
    answer = []

    for i in range(len(genres)):

        if genres[i] in total_plays:
           total_plays[genres[i]] += plays[i]
           play_list[genres[i]].append((i, plays[i]))
        else:
            total_plays[genres[i]] = plays[i]
            play_list[genres[i]] = [(i, plays[i])]

    total_plays_items = list(total_plays.items())
    total_plays_items.sort(key=lambda x: x[1], reverse=True)

    for g, _ in total_plays_items:
        play_list[g].sort(key=lambda x: x[1], reverse=True)
        answer.append(play_list[g][0][0])

        if len(play_list[g]) != 1:
            answer.append(play_list[g][1][0])

    return answer

