hash_table = list([i for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: #해쉬 테이블에 값이 들어있다면
        for index in range(hash_address,len(hash_table)):  #비어있는 공간을 탐색
            if hash_table[index] == 0:  #비어있는 공간을 찾아서 값을 저장
                hash_table[index] = [index,value]
                return
            elif hash_table[index][0] == index_key:   #키 값이 같은 경우  그 위치의 값을 업로드
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0 :
       for index in range(hash_address, len(hash_table)):
           if hash_table[index] == 0: #찾고자 하는 값이 해쉬 테이블에 없음
               return None
           elif hash_table[index][0] == index_key:
               return hash_table[index][1]
    else:
        return None