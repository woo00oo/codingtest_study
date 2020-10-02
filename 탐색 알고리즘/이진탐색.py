def binary_search(data,search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    #찾고자하는 숫자를 바로 찾았을 경우 ( 리스트의 가운데에 위치했을 경우)
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:],search)
        else:
            return binary_search(data[:medium],search)



