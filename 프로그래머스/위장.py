# 해시 자료구조 사용
# 경우의 수를 생각
# 각 경우를 모두 곱해주면 되는데 부위별로 있는 옷의 갯수에서 아무것도 안입는 경우가 있을 수 있으니 +1을 해준다.
# 또 모두 안입는 경우는 없다고 했으니 최종 곱한 값에서 -1을 해준다.

def solution(clothes):
    answer = {}

    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)

    return cnt - 1