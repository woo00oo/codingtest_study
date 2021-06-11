# 그리디 알고리즘
# 물병의 개수가 num일때, 최대로 합칠 수 있는 개수를 반환하는 함수 = mySum(num)
# 2로 나누었을 때 몫이 묶인 물병의 수가 되고, 나머지가 묶이지 않은 물병의 수가 된다.
# answer는 N에서 시작하여 1씩 증가하면서 mySum(answer)가 K 이하가 되는 첫번째 수를 구한다.
# 그 수가 최소로 더 필요한(더 사야할)물병의 수가 된다.

def mySum(num):
    ans = 0
    while True:
        bottle = num // 2
        remainder = num % 2
        ans += remainder
        num = bottle
        if num == 0:
            break
    return ans

N, K = map(int, input().split())

if K >= N:
    print(0)
else:
    answer = N
    while True:
        if mySum(answer) <= K:
            print(answer-N)
            break
        else:
            answer += 1