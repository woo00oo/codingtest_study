#문제풀이
#   문제에서 요구하는 것 : n개의 센서들은 k개의 구간으로 나눈것과 동일
#   센서 위치를 입력받아 오름차순으로 정렬
#   k개 n 보다 같거나 클 경우 모든 센서에 집중국을 설치하면 되므로 답은 0
#   그 이외의 경우 각 센서의 거리를 전부 구해 dis에 저장후 내림차순으로 정렬
#   센서들을 k구간으로 나눠야 하므로 k-1번만큼 반복을 돌며 값이 가장 큰 원소부터 차례로 제거함.
#   남은 원소들의 합을 구하여 출력.

N = int(input())
K = int(input())
li = sorted(list(map(int, input().split())))
dis = list()

if K >= N:
    print(0)
    exit(0)

for i in range(1, N):
    dis.append(li[i]-li[i-1])
dis.sort(reverse=True)

for _ in range(K-1):
    dis.pop(0)

print(sum(dis))