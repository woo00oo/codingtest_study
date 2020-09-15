
#내가 생각한 코드
#정확성 테스트는 빠르게 통과하였지만
#효율성 테스트에는 통과하지 못하여 시간을 조금 두어 생각해보았다.
"""
def solution(prices):
    answer = []
    for index1,i in enumerate(prices):
        count = 0
        for index2,j in enumerate(prices):
            if i <= j and index1 < index2:
                count += 1
            elif index1 >= index2:
                continue
            else:
                count += 1
                break
         answer.append(count)

    return answer
"""
# count값을 증가 시켜 마지막에 append를 하는 것이 아닌 리스트 원소값을 0으로 초기화 하여 바로바로 +1를 해주는 방법.


def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[i]>prices[j]:
                break

    return answer

prices = [1,2,3,2,3]
print(solution(prices))