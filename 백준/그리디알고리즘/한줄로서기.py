# total = int(input())
# arr = list(map(int,input().split()))
# arr_index = [(i+1,j) for i,j in enumerate(arr)]
# du = [(i+1,j) for i,j in enumerate(arr)]
# arr_index.sort(key=lambda x: x[1])
# du.sort(key= lambda x:x[1])
#
# arr_index_ex = []
# for i in range(1,total):
#     if arr_index[i][1] == arr_index[i-1][1]:
#         du.remove(arr_index[i])
#         arr_index_ex.append(arr_index[i])
#
#
# arr_index_ex.sort(key=lambda x:x[1],reverse=True)
# arr_index = du + arr_index_ex
#
# print(arr_index)
# for i in range(total):
#     print(arr_index[i][0], end=' ')

# 간단하게 생각하자 ....

n = int(input())

arr = list(map(int,input().split()))

answer = list()

for i in range(n):
    answer.insert(arr[n-1-i],n-i)


print(*answer)