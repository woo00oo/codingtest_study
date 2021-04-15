# 단계 별로 요구사항에 맞게 순차적으로 구현해 나가면 된다.
# 예외 상황 : 리스트의 길이를 잘 생각하여 인덱스 예외가 뜨지 않도록 주의 하자

def solution2(new_id):
    # 1단계 -> 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    new_id = list(new_id)

    S = "~!@#$%^&*()=+[{]}:?,<>/"

    # 2단계 -> 특수문자 제거
    removed = 0
    for i in range(len(new_id)):
        i -= removed
        if new_id[i] in S:
            del new_id[i]
            removed += 1
    # 3단계
    removed = 0
    for i in range(1, len(new_id)):
        i -= removed
        if new_id[i] == '.':
            if new_id[i - 1] == new_id[i]:
                del new_id[i]
                removed += 1


    # 4단계
    while True:
        if new_id[0] != '.' and new_id[-1] != '.':
            break
        if new_id[0] == '.':
            del new_id[0]
            if len(new_id) == 0:
                break
        if new_id[-1] == '.':
            del new_id[-1]
            if len(new_id) == 0:
                break

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계
    new_id = new_id[:15]
    while True:
        if new_id[-1] != '.':
            break
        del new_id[-1]


    #7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return ''.join(new_id)

## 다른 사람 풀이 훨씬 간단.
# isalpha() -> 알파벳인지 확인
# isdigit() -> 숫자인지 확인
# isalnum() -> 알파벳 or 숫자인지 확인
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalnum() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer



