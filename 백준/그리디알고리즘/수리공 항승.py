#문제풀이:
#   한 곳을 막기 위해서는 테이프의 길이 1만큼 필요함.
#   오름차순으로 정렬후 첫번째 새는 곳을 주어진 테이프의 길이로 막는다
#   r 은 위의 테이프 길이만큼 얼마나의 위치 만큼 막아졌는지
#   arr을 1부터 돌면서 r보다 작은 값(이미 테이프로 감싸짐)은 continue
#   그렇지 않은 경우에는 새로 테이프를 붙혀야하기 때문에 r을 구하고 count를 1 증가

N, L = map(int,input().split())
arr = sorted(list(map(int,input().split())))
count = 1
r = arr[0] + (L-1)
for i in range(1,N):
    if arr[i] <= r:
        continue
    count += 1
    r = arr[i] + (L - 1)
print(count)