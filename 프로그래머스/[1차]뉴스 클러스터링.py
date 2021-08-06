# 1차 풀이 : 실패
# 이유 : 합집합 구하는 과정에서 arr2의 원소가 arr1 배열에는 없지만 중복된 원소일 경우 한번만 append하는 것이 아닌 중복 횟수만큼 append 되어야함.

def solution(str1, str2):
    arr1, arr2 = [], []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            arr1.append(str1[i:i+2].lower())

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            arr2.append(str2[i:i+2].lower())

    if len(arr1) == 0 and len(arr2) == 0:
        return 1 * 65536

    intersection = []
    union = []

    # 교집합, 합집합 구하기
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            if arr1[i] not in intersection:
                inter_cnt = min(arr1.count(arr1[i]), arr2.count(arr1[i]))
                for _ in range(inter_cnt):
                    intersection.append(arr1[i])

            if arr1[i] not in union:
                uni_cnt = max(arr1.count(arr1[i]), arr2.count(arr1[i]))
                for _ in range(uni_cnt):
                    union.append(arr1[i])
        else:
            union.append(arr1[i])

    for i in range(len(arr2)):
        if arr2[i] not in union:
            union.append(arr2[i])
        # elif arr2[i] not in arr1:  -> 이 로직을 추가하면 문제풀이 해결 가능.
        #     union.append(arr2[i])

    return int(len(intersection) / len(union) * 65536)


'''
2차 풀이 
Counter 모듈을 잘 활용하자 => 문제에서 요구한 조건들을 복잡한 로직이 아닌 단순하게 해결 가능

- Counter 객체는 교집합과 합집합 연산이 가능하다. 문제에서 제시된 조건대로 중복 원소의 교집합일 경우 작은값, 합집합일 경우 큰 값으로 계산된다

- elements() 카운터 된 숫자만큼의 요소를 리턴 

 ex) 'a': 2, 'b':1 => ['a', 'a', 'b']를 리턴 


'''

from collections import Counter


def solution(str1, str2):
    arr1, arr2 = [], []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            arr1.append(str1[i:i+2].lower())

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            arr2.append(str2[i:i+2].lower())

    if len(arr1) == 0 and len(arr2) == 0:
        return 1 * 65536


    Counter1 = Counter(arr1)
    Counter2 = Counter(arr2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
