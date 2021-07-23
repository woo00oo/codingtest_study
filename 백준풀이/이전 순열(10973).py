from sys import stdin


def prev_permutation(lst):
    length = len(lst) - 1
    i, j, k = [length for _ in range(3)]

    while i > 0 and lst[i - 1] <= lst[i]:
        i -= 1

    if not i:
        return 0

    while lst[i - 1] <= lst[j]:
        j -= 1

    lst[i - 1], lst[j] = lst[j], lst[i - 1]

    while i < k:
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1
    return lst

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
ret = prev_permutation(nums)
print(-1) if not ret else print(*nums)