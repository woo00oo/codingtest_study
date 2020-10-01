def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [ item for item in data[1:] if pivot >item]
    right = [ item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)


#퀵소트는 pivot(기준점을 정해 ) pivot보다 작은수는 왼쪽 큰수는 오른쪽에 배치하여 , 재귀호출을 통하여 리스트의 길이가 1까지 반복해서 호출 한 후
# 합치는 정렬 방법
