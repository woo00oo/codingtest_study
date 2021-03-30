# 윤년 => 2월이 29일까지 있는 해
# 해당 날짜가 1월 1일부터 며칠이 지났는지 total 변수를 구해준다.
# total 를 7로 남은 나머지가 무슨 요일인지 구해주면 해당 문제를 해결할 수 있다.

def solution(a, b):
    total = 0
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    for i in range(1,a):
        total += months[i]
    total += b
    day = total % 7

    return days[day]

print(solution(5,24))