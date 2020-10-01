def solution(numbers):
    numbers = list(map(str, numbers)) #int형 원소 -> str형 원소로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers))) #int로 변환하고 다시 string으로 변환 하는 이유 : [0,0,0,0]일경우 0000이 아니라 0으로 반환!


numbers = [31,32,3, 34, 5, 9]

print(solution(numbers))

#lambda 인자 : 표현식
#map(함수,리스트) -> 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨후, 새로운 결과를 새로운 리스트에 담아줌.
#join함수: 리스트에서 -> 문자열로 변환