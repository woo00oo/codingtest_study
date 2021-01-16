#시간 초과 2중 for문
# N = int(input())
# M = int(input())
# N_list = list(map(int,input().split()))
# count = 0
#
# for i in range(N):
#     for j in range(i+1,N):
#         if N_list[i] + N_list[j] == M:
#             count += 1
#
# print(count)

#문제 해결:
#   for문을 한번 만 사용
N = int(input())
M = int(input())
N_list = list(map(int,input().split()))
count = 0

for i in range(N):
    find_num = M - N_list[i]
    if find_num in N_list:
        count += 1

print(count//2)


# 다른 문제 풀이: 투포인터 활용
# 1. 리스트를 정렬
# 2. 양끝 값에서(i= 0 , j = n-1)시작해서 둘의 합이 m과 같으면 cnt에 1을 더하고 위치를 하나씩 옮긴다.( i = i+1, j =j -1)
# 3. 양 끝 값에서 시작해서 둘의 합이 m보다 작으면 왼쪽의 작은 값을 크게 만들어야 한다. (i = i+1)
# 4. 양끝 값에서 시작해서 둘의 합이 m보다 크면 왼쪽의 큰 값을 작게 만들어야 한다(j= j-1)

n = int(input())
m = int(input())
nums = sorted(list(map(int,input().split())))
cnt = 0
i,j = 0, n-1
while i<j:
    if nums[i] + nums[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] < m:
        i +=1
    else:
        j -= 1

print(cnt)