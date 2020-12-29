#문제풀이 :
#   (인덱스,값)으로 이루어진 리스트를 만든다.
#   count = 출력한 횟수를 나타낸다.
#   max함수를 활용하여 리스트 맨앞에 있는 원소가 리스트의 최대값인지 확인
#   1) 최대값이 아니라면
#       리스트의 맨 뒤로 보낸다.
#   2) 최대값이라면
#       count를 1 증가 시킨다 ( 출력했다는 의미)
#   2-1) 출력한 원소가 location이라면
#       반복문을 종료하고 count를 리턴
#   2-2) 출력한 원소가 location이 아니라면
#       리스트에서 pop(0)해주고 반복문을 계속 돈다.

def solution(priorities, location):
    queue = [(x,y) for x,y in enumerate(priorities)]

    count = 0
    while True:
        if queue[0][1] == max(queue,key=lambda x:x[1])[1]:
            count += 1

            if queue[0][0] == location:
                break
            else:
                queue.pop(0)

        else:
            queue.append(queue.pop(0))

    return count


