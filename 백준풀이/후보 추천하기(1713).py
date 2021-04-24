# 딕셔너리 자료 구조 사용
# key : 학생 번호 value = [추천수, 들어온 순서]

N = int(input())
total = int(input())
arr = list(map(int,input().split()))
answer = dict()

for i in range(total):
    # 사진틀이 N보다 적을 경우(사진틀이 남아있을 경우)
    if len(answer) < N:
        # 새로운 학생 번호가 들어온 경우
        if arr[i] not in answer:
            answer[arr[i]] = [1, i] # key를 학생 번호, [추천수 1 들어온 순서] 를 저장
        # 기존 사진틀에 학생일 경우
        else:
            answer[arr[i]][0] += 1 #추천수를 1 증가 시켜줌
    # 사진틀이 꽉 찼을 경우( 새로운 학생이 들어오면 기존 학생 중 한명을 삭제 시켜야함)
    else:
        # 기존에 있던 학생이 들어온 경우
        if arr[i] in answer:
            answer[arr[i]][0] += 1 # 추천수를 1 증가 시켜줌
        # 새로운 학생이 들어온 경우
        else:
            # 추천수가 가장 적고 가장 나중에 들어온 학생 한명을 삭제 시킴
            del_list = list(sorted(answer.items(), key=lambda x: (x[1][0], x[1][1])))
            del_key = del_list[0][0]
            del answer[del_key]
            # 새로운 학생을 추가 시킴
            answer[arr[i]] = [1, i]
answer = sorted(list(answer.keys()))
print(*answer)