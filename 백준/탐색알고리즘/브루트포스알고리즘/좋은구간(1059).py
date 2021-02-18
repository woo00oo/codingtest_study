# N를 포함한 구간 = end - start
# N 미만의 가능한 숫자 * N 초과의 가능한 숫자 = (N - start) * (end - N)
# start = 1로 초기화 해줘야 한다. N이 S에서 가장 작은 값일 경우 1 ~ N까지의 구간을 구해줘야 하기 때문 => 0 ~ N까지의 구간이 아니다.

L = int(input())
S = sorted(list(map(int, input().split())))
N = int(input())
start = 1
end = 0
if N in S:
    print(0)

else:
    for i in S:
        if N > i:
            start = i + 1
        else:
            end = i - 1
            break
    print(end - start + (N - start) * (end - N)) 