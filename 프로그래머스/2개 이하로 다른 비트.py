# 짝수인 경우 : 가장 뒤에 있는 0을 1로 변환
# 홀수인 경우 : 가장 뒤에 있는 0을 1로 바꾸고, 변환된 인덱스 + 1의 값을 0으로 변환

# find(), rfind() : 문자열 내부에서 특정문자가 어디에 위치하는지 찾을때 사용
# find() 왼쪽부터 찾음, rfind() 오른쪽부터 찾음

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + format(number, 'b'))
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        # 홀수라면
        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer