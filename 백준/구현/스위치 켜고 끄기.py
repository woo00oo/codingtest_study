# 단순 구현 문제 였지만, 마지막 출력 규칙을 제대로 읽지 않아 시간을 낭비함.
# 문제 꼼꼼히 읽기!

def man(number):
    for i in range(1,N + 1):
        if i % number == 0:
            switch[i] = int(not switch[i])

def woman(number):
    switch[number] = int(not switch[number])

    i = 1
    while True:

        if 0 < number + i < N + 1 and 0 < number - i < N + 1:
            if switch[number+i] == switch[number-i]:
                switch[number+i] = int(not switch[number+i])
                switch[number-i] = int(not switch[number-i])
                i += 1
            else:
                break
        else:
            break

N = int(input())
switch = [0]
switch += list(map(int,input().split()))
student_N = int(input())
students = []
for _ in range(student_N):
    gender, number = map(int,input().split())
    students.append((gender,number))
for i in range(student_N):
    if students[i][0] == 1:
        man(students[i][1])
    else:
        woman(students[i][1])
if N <= 20:
    print(*switch[1:])
else:
    for i in range(1,N+1):
        print(switch[i], end=' ')
        if i % 20 == 0:
            print(' ')

