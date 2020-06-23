def solution(heights):
    answer = []
    success = 1
    print(heights)
    for index, top in enumerate(reversed(heights)):
        print(len(heights)-(index+1)+1,top)
        success = 0
        for idx,res in enumerate(reversed(heights)):
            if res > top and (len(heights)-(index+1)+1) > (len(heights)-(idx+1))+1:
                answer.append((len(heights)-(idx+1))+1)
                print()
                success = 1
                break
        if success==0:
            answer.append(0)
            print(top+100)

    return list(reversed(answer))


heights = [1,5,3,6,7,6,5]


print(solution(heights))