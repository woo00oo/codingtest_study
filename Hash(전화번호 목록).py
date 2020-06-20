def solution(phone_book):
    for number in phone_book:
        num_index = phone_book.index(number)
        del phone_book[num_index]
        for number2 in phone_book:
            if(number == number2[0:len(number)]):
                phone_book.insert(num_index, number)
                return False
        phone_book.insert(num_index,number)
    return True



tell = ['21192','119','97674223',]

result = solution(tell)

print(tell)
print(result)