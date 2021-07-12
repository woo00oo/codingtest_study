n = int(input())
student = []
for _ in range(n):
    name, day, month, year = input().split()

    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month

    student.append((name, year + month + day))

student.sort(key=lambda x: x[1])

print(student[-1][0])
print(student[0][0])