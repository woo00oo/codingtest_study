import sys

N = int(input())
people = set()
for _ in range(N):
    name, recode = sys.stdin.readline().split()
    if recode == 'enter':
        people.add(name)
    elif recode == 'leave':
        people.remove(name)

people = sorted(list(people), reverse=True)
for i in range(len(people)):
    print(people[i])