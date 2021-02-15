#문제해결 :
#   그리디 알고리즘을 활용하여 풀 수 있다.
n = int(input())
if n in [1,3]:
    result = -1
elif (n % 5) % 2 == 0:
    result = n//5 + (n % 5)//2
else:
    result = ((n // 5)-1) + ((n % 5+5)//2)
print(result)