# 정확성은 통과 하였지만, 효율성은 불통과
def solution_err(info, query):
    answer = []
    for q in range(len(query)):
        cnt = 0
        select = query[q].split(' and ')
        food, score = select[-1].split(' ')
        del select[-1]
        select.append(food)
        select.append(score)
        for i in range(len(info)):
            data = info[i].split(' ')
            check = True
            for s1,s2 in zip(data,select):
                if s2 == '-':
                    continue
                if s1.isdigit():
                    if int(s1) < int(s2):
                        check = False
                elif s1 != s2:
                    check = False

            if check:
                cnt += 1

        answer.append(cnt)

    return answer

# '-'를 포함한 조건상의 모든 경우에 대해 데이터를 저장하고, 이진 탐색을 통해 주어진 점수값보다 높은 점수를 가진 데이터의 갯수를 빠르게 얻어낸다.
# https://dev-note-97.tistory.com/131 참고

from itertools import combinations


def solution(info, query):
    answer = []
    db = {}
    for i in info:  # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]  # 조건들만 모으고, 점수 따로
        score = int(temp[-1])
        for n in range(5):  # 조건들에 대해 조합을 이용해서
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:  # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:  # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():  # 딕셔너리 내 모든 값 정렬
        value.sort()

    for q in query:  # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer