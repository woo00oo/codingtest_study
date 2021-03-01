# 이분탐색을 활용한 문제 풀이

N = int(input())
N_li = sorted(list(map(int, input().split())))
M = int(input())
M_li = list(map(int,input().split()))
answer = list()

for number in M_li:
    check = False
    start = 0
    end = N - 1
    while end - start >= 0:
        mid = (start + end) // 2
        if N_li[mid] == number:
            answer.append(1)
            check = True
            break
        elif N_li[mid] > number:
            end = mid - 1
        else:
            start = mid + 1
    if not check:
        answer.append(0)

print(*answer)

# set 자료구조를 활용한 문제 풀이( 시간이 더 효율적이다)
N = int(input())
N_li = set(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))

for number in M_li:
    if number in N_li:
        print(1, end=' ')
    else:
        print(0, end=' ')