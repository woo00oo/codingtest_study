import math

def solution(progresses, speeds):
    answer = []
    successtime = []
    count = 1
    maxnumber = 0
    for work,time in zip(progresses,speeds):
        successtime.append(math.ceil((100 - work) / time))

    for index, release in enumerate(successtime):
        if release > maxnumber:
            maxnumber = release
            for idx, day in enumerate(successtime):
                if release >= day and idx > index :
                    count +=1
                elif day > release and idx > index :
                    break
            answer.append(count)
            count =1
    return answer


