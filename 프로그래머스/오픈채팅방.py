# 첫번째 풀이 : 실패
#   dict 자료구조를 사용해야겠다는 생각은 좋았으나 이미 값이 answer로 append하기 때문에 수정사항에 대해 변경이 이루어 지지 않음.


def solution(record):
    answer = []
    user = dict()
    for idx, s in enumerate(record):
        chat = s.split(' ')

        if chat[0] == 'Enter':
            user[chat[1]] = chat[2]
            answer.append(user[chat[1]] +'님이 들어왔습니다.')
        elif chat[0] == 'Leave':
            answer.append(user[chat[1]] +'님이 나갔습니다.')
        else:
            user[chat[1]] = chat[2]

    return answer


## 두번째 풀이
# 동일하게 ID를 키 값 닉네임을 벨류로 관리를 한다.
# 로그를 맨 나중에 append 함으로써 변경사항들이 반영 되도록한다.

def solution(record):
    answer = []
    dic = {}

    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % dic[sentence_split[1]])

    return (answer)