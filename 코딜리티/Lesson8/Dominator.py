def solution(A):
    cnt_dict = dict()

    for i in range(len(A)):
        if A[i] not in cnt_dict:
            cnt_dict[A[i]] = [i]
        else:
            cnt_dict[A[i]].append(i)

    cnt_dict_items = list(cnt_dict.items())

    for i in range(len(cnt_dict_items)):
        if len(cnt_dict_items[i][1]) > len(A)//2:
            return cnt_dict_items[i][1][0]

    return -1


