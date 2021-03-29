# 0, 1, 2 삼진법이 아닌 1,2,3 삼진법으로 접근
# 삼진법에 0이 포함되지 않기 때문에 divmod(n,3)이 아니라 divmod(n-1,3)
# divmode(a,b) a를 b로 나누었을 때 몫과 나머지를 튜플의 형태로 return

def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1,3)
        return solution(q) + '124'[r]