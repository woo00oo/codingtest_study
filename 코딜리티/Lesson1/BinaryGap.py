# 내풀이 : O(N)

def solution(N):
    answer = 0
    # 10진수 -> 2진수 변환
    binary_num = format(N, 'b')

    binary_num = str(binary_num)

    # 2진갭 체크
    left = -1
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            if left == -1:
                left = i
            elif left != -1:
                gap = i - left - 1
                if gap > answer:
                    answer = gap
                left = i

    return answer

# 다른사람 풀이 : O(N)
# 시간 복잡도는 같지만, 로직을 더 단순하게 구성하여 해결한 거 같다.
# 1이 나오기 전까지 0의 개수를 더해 누적된 1의 개수의 최대값이 문제에서의 정답

def solution2(N):
    answer = 0
    # 10진수 -> 2진수
    binary_num = format(N, 'b')
    binary_num = str(binary_num)

    cnt = 0
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            if cnt > answer:
                answer = cnt
            cnt = 0
        else:
            cnt += 1

    return answer


# 파이썬 진법 변환 메소드

# 10진수 -> 2, 8, 16 진수
# format(value, 'b')
# format(value, 'o')
# format(value, 'x')

# 2, 8, 16 진수 -> 10진수
# int(value, 2)
# int(value, 8)
# int(value, 16)


