# 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스크로 데이터를 추가로 뒤에 연결 시켜서 저장하는 기법
# value값 외에도 index_key값을 저장 시켜 충돌이 일어났을 경우 원하는 value를 인덱스 키로 구별 하여 접근
#ex) [[1,123456],[2,123123]]



import hashlib

hash_table = list([i for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode()) #받은 데이터를 인코딩(바이트로 바꿔줌)
    hex_dig = hash_object.hexdigest() #16진수로 변환
    return int(hex_dig,16)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    #충돌 났을 경우
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            #존재하는 index_key에 value를 덮어쓸 경우
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None