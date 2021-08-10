import sys


def cross(r):
    if r == 0:
        return people[0]
    if r == 1:
        return people[1]
    if r == 2:
        return people[0] + people[1] + people[2]

    if people[0] + people[r-1] > 2 * people[1]:
        return people[0] + 2 * people[1] + people[r] + cross(r-2)
    else:
        return 2 * people[0] + people[r-1] + people[r] + cross(r-2)


N = int(sys.stdin.readline().strip())
people = []
for _ in range(N):
    people.append(int(sys.stdin.readline().strip()))
people.sort()
print(cross(N-1))