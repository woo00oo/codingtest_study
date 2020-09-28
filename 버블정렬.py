def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-1-index): #1패턴을 돌때마다 가장 큰 index는 리스트의 가장 뒤로 가므로 재반복해서 비교할 필요가 없음
            if data[index2] > data[index2+1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]
                swap = True
            if swap == False :#넘어온 data가 이미 정렬이 되어있을 경우
                break
    return data