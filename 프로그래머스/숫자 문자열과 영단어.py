# replace -> 변수 할당 (적용)

def solution(s):
    answer = 0
    word = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for key in word.keys():
        s = s.replace(key, word[key])

    return int(s)