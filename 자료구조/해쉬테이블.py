hash_table = list([i for i in range(10)])

#해싱 함수
def hash_func(key):
    return key % 5

#해쉬 테이블에 값을 저장하는 함수
def storage_data(data,value):
    key = ord(data[0]) #문자의 아스키 코드를 돌려주는 함수
    hash_address = hash_func(key)
    hash_table[hash_address] = value

#해쉬 테이블에서 값을 가져오는 함수
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]




