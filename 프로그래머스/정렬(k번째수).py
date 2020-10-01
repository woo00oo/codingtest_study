def solution(array, commands):
    answer = []
    arraySort =[]
    for i in commands:
        arraySort  = array[i[0]-1:i[1]]
        arraySort.sort()
        answer.append(arraySort[i[2]-1])

    return answer





testArray = [1,5,2,6,3,7,4]
testCommands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(testArray,testCommands))