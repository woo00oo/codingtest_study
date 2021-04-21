# 문제를 구현하는 것 쉽지만 소수점 오차로 인해 정답처리가 되지 않았다.

N, K = map(int,input().split())
numbers = []
answer1, answer2 = 0, 0
for _ in range(N):
    numbers.append(float(input()))
numbers.sort()
if K != 0:
    arr1 = numbers[K:-K]
else:
    arr1 = numbers
arr2 = numbers
for i in range(1,K+1):
    arr2[i-1] = arr1[0]
    arr2[-i] = arr1[-1]

answer1 = sum(arr1) / len(arr1)
answer2 = sum(arr2) / len(arr2)

print("%.2f" % answer1)
print("%.2f" % answer2)

#################
# 소숫점을 메모리에 저장할 때 대부분의 수에서 오차가 발생하게 된다.
# 소숫점 아래가 과 같은 수가 아니면 무한소수가 되기 때문에 무조건 오차가 발생할 수 밖에 없다.
# 따라서 출력할 때, 반올림에서 문제가 생길 수 있는데, 예를 들면 다음과 같은 경우다.
# 4.45로 저장되어야 할 수가 4.44999999999999로 저장된 경우. 이 경우에는 소숫점 아래 셋째 자리에서 반올림하면 4.5가 되어야 할 수가 4.4가 돼 버린다.
# 따라서 적당한 수를 더해줌으로써 이를 해결해야되는데, 1e-9 정도의 수를 더해줌으로써 해결했다. 다만 1e-15부터는 의미가 없게되니 주의해야한다. 1e-15는 0이 된다.
# 1e - 9 => 1 * 10의 -9승
# 1e + 5 => 1 * 10의 5승


import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[float(input()) for _ in range(n)]
arr.sort()
print("%.2f"%(sum(arr[k:n-k])/(n-2*k)+1e-9))
print("%.2f"%((sum(arr[k:n-k])+(k*arr[k])+(k*arr[n-k-1]))/n+1e-9))