from sys import stdin
from itertools import combinations

N = int(stdin.readline().strip())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]
numbers = {i for i in range(1, N+1)}
start_team = list(set(combinations(numbers, N//2)))
link_team = []
for i in range(len(start_team)):
    num = set(start_team[i])
    link_team.append(tuple(numbers-num))

answer = []
for i in range(len(start_team)):
    start_skill, link_skill = 0, 0
    for x in range(len(start_team[i])-1):
        for y in range(x, len(start_team[i])):
            start_skill += S[start_team[i][x]-1][start_team[i][y]-1] + S[start_team[i][y]-1][start_team[i][x]-1]
            link_skill += S[link_team[i][x]-1][link_team[i][y]-1] + S[link_team[i][y]-1][link_team[i][x]-1]

    answer.append(abs(start_skill - link_skill))

print(min(answer))
