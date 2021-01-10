N, S, R = list(map(int,input().split()))
S_list = list(map(int,input().split()))
R_list = list(map(int,input().split()))
answer = 0
for i in S_list:
    if i-1 in R_list:
        R_list.remove(i-1)
    elif i+1 in R_list:
        R_list.remove(i+1)
    else:
        answer +=1
print(answer)