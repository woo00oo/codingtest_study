# math.gcd(num1, num2) => 최대 공약수를 구해주는 메소드
# 최소 공배수 => num1, num2 // 최대 공약수

import math

num1, num2 = map(int,input().split())
print(math.gcd(num1,num2))
print(num1 * num2 // math.gcd(num1, num2))