#문제 해결 : 이진 탐색으로 풀어보려고 하였지만 시간복잡도가 약 NlogM *20 약 1억이 넘는 수라 시간초과가 뜸.


N, M = list(map(int,input().split()))

N_list = [input() for _ in range(N)]
M_list = [input() for _ in range(M)]
N_list.sort()
M_list.sort()

for n in N_list:
    start = 0
    end = M-1

    while start <= end:
        mid = (start + end) // 2

        if M_list[mid] == n:
            print(M_list[mid])
            break
        elif M_list[mid] > n:
            end = mid - 1
        else:
            start = mid + 1

#   교집합으로 간단하게 해결.

N, M = list(map(int,input().split()))

N_list = {input() for _ in range(N)}
M_list = {input() for _ in range(M)}

answer = sorted(list(N_list&M_list))
print(len(answer))
for i in answer:
    print(i)