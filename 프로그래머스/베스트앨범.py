def solution(genres, plays):
    music = dict()
    music_play = dict()
    answer = []

    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = [(plays[i], i)]
            music_play[genres[i]] = plays[i]
        else:
            music[genres[i]].append((plays[i], i))
            music_play[genres[i]] += plays[i]

    genres_li = sorted(music_play.items(), key=lambda x: x[1], reverse=True)[:2]

    for genre in genres_li:
        li = sorted(music[genre[0]], key=lambda x: (-x[0], x[1]))
        if len(li) > 1:
            answer.append(li[0][1])
            answer.append(li[1][1])
        else:
            answer.append(li[0][1])

    return answer


from collections import defaultdict
from operator import itemgetter

def solution2(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play

    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]

    final_dict = defaultdict(lambda: [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))

    answer = []

    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)

        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])

    return answer



