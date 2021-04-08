# 문제는 해결하였지만 코드가 지저분하다. 길다
# 아래 코드 처럼 함수화를 잘 시키고 중복되는 코드를 줄이자.

def solution(numbers, hand):
    answer = ''
    right = (3,2)
    left = (3,0)
    for num in numbers:
        if num == 1:
            left = (0,0)
            answer += 'L'
        elif num == 2:
            left_l = abs(left[0] - 0) + abs(left[1]-1)
            right_l = abs(right[0]-0) + abs(right[1]-1)
            if left_l < right_l:
                left = (0,1)
                answer += 'L'
            elif left_l > right_l:
                right = (0,1)
                answer += 'R'
            else:
                if hand == 'left':
                    left = (0,1)
                    answer += 'L'
                else:
                    right = (0,1)
                    answer += 'R'
        elif num == 3:
            right = (0,2)
            answer += 'R'
        elif num == 4:
            left = (1,0)
            answer += 'L'
        elif num == 5:
            left_l = abs(left[0]-1) + abs(left[1]-1)
            right_l = abs(right[0]-1) + abs(right[1]-1)
            if left_l < right_l:
                left = (1,1)
                answer += 'L'
            elif left_l > right_l:
                right = (1,1)
                answer += 'R'
            else:
                if hand == 'left':
                    left = (1,1)
                    answer += 'L'
                else:
                    right = (1,1)
                    answer += 'R'
        elif num == 6:
            right = (1,2)
            answer += 'R'
        elif num == 7:
            left = (2,0)
            answer += 'L'
        elif num == 8:
            left_l = abs(left[0] - 2) + abs(left[1] - 1)
            right_l = abs(right[0] - 2) + abs(right[1] - 1)
            if left_l < right_l:
                left = (2, 1)
                answer += 'L'
            elif left_l > right_l:
                right = (2, 1)
                answer += 'R'
            else:
                if hand == 'left':
                    left = (2, 1)
                    answer += 'L'
                else:
                    right = (2, 1)
                    answer += 'R'
        elif num == 9:
            right = (2,2)
            answer += 'R'
        else:
            left_l = abs(left[0] - 3) + abs(left[1] - 1)
            right_l = abs(right[0] - 3) + abs(right[1] - 1)
            if left_l < right_l:
                left = (3, 1)
                answer += 'L'
            elif left_l > right_l:
                right = (3, 1)
                answer += 'R'
            else:
                if hand == 'left':
                    left = (3, 1)
                    answer += 'L'
                else:
                    right = (3, 1)
                    answer += 'R'
    return answer
##################################

def get_distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    hand = 'R' if hand == 'right' else 'L'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = str(number)
            continue
        if number in [3, 6, 9]:
            answer += 'R'
            right = str(number)
            continue
        if number in [2, 5, 8, 0]:
            dis1 = get_distance(left, number)
            dis2 = get_distance(right, number)
            if dis1 > dis2:
                answer += 'R'
                right = str(number)
            if dis1 < dis2:
                answer += 'L'
                left = str(number)
            if dis1 == dis2:
                answer += hand
                if hand == 'R':
                    right = str(number)
                if hand == 'L':
                    left = str(number)
    return answer

