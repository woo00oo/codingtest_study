number = int(input())
count = 99
if number < 100:
    print(number)
else:
    for i in range(100,number+1):
        number_1 = i % 10
        number_10 = (i // 10) % 10
        number_100 = (i // 100) % 10
        if 2*number_10 == number_1 + number_100:
            count += 1
    if number == 1000:
        count -=1
    print(count)