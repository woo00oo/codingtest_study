def solution(priorities, location):
    count = 1
    searchNum = priorities[location]
    max = searchNum
    for i in priorities :
        if searchNum < i :
            count +=1
            max = i
    if max != searchNum :
        for index,i in enumerate(priorities):
            if priorities.index(max) < index and searchNum == i and index != location:
                count +=1


    return count

priorities = [1, 1, 9, 1, 1, 1]
location = 3

print(solution(priorities,location))