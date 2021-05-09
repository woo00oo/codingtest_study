# 첫번째 시도 : 하나의 리스트를 만들어서 index와 값으로 구분 =>시간 초과
# 검색 성능이 훨씬 뛰어난 딕셔너리(해시) 자료구조를 사용 => key가 Id, name인 딕셔너리 생성

N, M = map(int, input().split())
monsters_id = dict()
monsters_name = dict()
for i in range(1, N+1):
    name = input()
    monsters_id[i] = name
    monsters_name[name] = i
for _ in range(M):
    question = input()
    if question.isalpha():
        print(monsters_name[question])
    elif question.isdigit():
        print(monsters_id[int(question)])