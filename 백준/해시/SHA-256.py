# SHA - 256 : 대표적인 해시 알고리즘

import hashlib

text = input()

encode_text = hashlib.sha256(text.encode())

#해시 결과 문자열 반환
print(encode_text.hexdigest())