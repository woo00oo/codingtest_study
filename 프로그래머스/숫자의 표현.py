# 문제풀이:
#   start, end 를 1로 주어 start가 n 이하일 경우까지
#   start ~ end를 모두 더한 합이 n보다 작은 경우에 end += 1 , 큰 경우 start += 1, 같은 경우에는 answer += 1, start +=1를 반복해 나간다.
def solution(n):
    answer = 0
    numbers = [i for i in range(n+1)]
    start, end = 1, 1

    while start <= n:
        Sum = sum(numbers[start:end+1])
        if Sum < n:
            end += 1
        elif Sum > n:
            start += 1
        else:
            answer += 1
            start += 1

    return answer

print(solution(15))