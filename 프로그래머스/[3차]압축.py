'''
정답 처리는 받았지만, 깔끔한 코드는 아닌 거 같다.
다음 입력을 받아오는 과정에서 조금 더 간결한 코드를 작성할 필요가 있어 보인다.

'''

def solution(msg):
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
           'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
           'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    answer = []
    msg_li = list(msg)
    num = 27
    check = 0
    for i in range(len(msg_li)):
        if i == len(msg_li) - 1 and check != 0:
            answer.append(dic[temp])

        if check != 0:
            check -= 1
            continue

        temp = msg_li[i]
        for j in range(i+1, len(msg_li)):
            if temp + msg_li[j] in dic:
                temp += msg_li[j]
                check += 1
            else:
                answer.append(dic[temp])
                dic[temp+msg_li[j]] = num
                num += 1
                break

        if i == len(msg_li) - 1:
            answer.append(dic[temp])

    return answer


##-----------------

'''
다른 사람 풀이

1) 기본 사전을 초기화 하는 부분이 단순하다.

2) 규칙성을 찾을 수 있다
    현재 글자 + 다음 글자가 사전에 없다면 w = c, c = c + 1
    현재 글자 + 다음글자가 사전에 있다면 w는 변화 없음, c = c + 1

'''

def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer
