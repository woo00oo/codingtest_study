# 첫번째 시도 -> in 메소드를 쓰게 되면 접두사가 아닌 중간에 있는 값이 겹칠 경우에도 False를 리턴하기 때문에 실패

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break

    return answer




# startswith() -> 찾고자 하는 문자열 A가 문자열 B의 맨 앞에 있는지의 여부를 알려줌.
# strB.startswith(strA,beg=0,end=len(string))
# strB[beg:end]에서 strA 문자열 찾기!
# 정렬을 하기 때문에 앞 뒤로만 비교를 해주면 된다.

def solution2(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

