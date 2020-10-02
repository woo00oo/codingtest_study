# 1000개의 데이터를 삽입정렬, 퀵 정렬로 정렬하는 함수를 각각 만들어보고, 각각의 정렬 시간을 출력하기

def inssertSort(data):
    for index in range(1,len(data)):
        for index2 in range(index,0,-1):
            if data[index2] < data[index2 -1]:
                data[index2],data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data

def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]
    return qsort(left) + [pivot] + qsort(right)

import datetime
import random
data_list = random.sample(range(10000),10000)
data_list2 = random.sample(range(10000),10000)
print("삽입 정렬 시작!" , datetime.datetime.now())
print(inssertSort(data_list))
print("삽입 정렬 종료!", datetime.datetime.now())
print("----------------------")
print("퀵 정렬 시작!" , datetime.datetime.now())
print(qsort(data_list))  # 파이썬에서는 재귀호출을 1000번으로 제한하고있음!
print("퀵 정렬 종료!", datetime.datetime.now())


