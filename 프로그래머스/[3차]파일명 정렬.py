def solution(files):
    sort_files = []
    answer = []
    for idx, file in enumerate(files):
        head = ''
        num_start = 0
        number = 0
        for i in range(len(file)-1):
            if not file[i].isdigit() and file[i+1].isdigit():
                head = file[:i+1].lower()
                num_start = i+1
                continue
            if file[i].isdigit() and not file[i+1].isdigit():
                number = int(file[num_start:i+1])
                break

        sort_files.append((head, number, idx, file))

    sort_files.sort(key=lambda x: (x[0], x[1], x[2]))
    for file in sort_files:
        answer.append(file[3])

    return answer

# ---
def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(t) for t in answer]   # 원래 형태로 문자열 만들어서 반환