N = int(input())
serial_numbers = []
for _ in range(N):
    serial_numbers.append(input())


for i in range(N):
    num_sum = 0
    for j in range(len(serial_numbers[i])):
        if serial_numbers[i][j].isdecimal():
            num_sum += int(serial_numbers[i][j])
    serial_numbers[i] = (serial_numbers[i], num_sum)

serial_numbers.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in range(N):
    print(serial_numbers[i][0])