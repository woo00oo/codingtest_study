import sys
# 시간초과
# 규칙을 찾아서 해결해야한다.
# N = int(input())
# books = list()
# answer = list()
# count = 0
# for _ in range(N):
#     book = int(sys.stdin.readline())
#     books.append(book)
#     answer.append(book)
# while books:
#     out_book = max(books)
#     if out_book != answer[0]:
#         count += 1
#         books.remove(out_book)
#         answer.remove(out_book)
#         answer.insert(0, out_book)
#     else:
#         books.remove(out_book)
# print(count)

# max로 비교할 값이 원래의 max보다 1 증가한 수인지 아닌지를 찾으면 된다.

n = int(input())
cnt = 0
L = [int(sys.stdin.readline())]
max = L[0]
for i in range(1,n):
    L.append(int(sys.stdin.readline()))
for i in range(1,n) :
    if L[i] > max :
        if max+1 != L[i] :
            cnt +=1
            max = L[i]
    else :
        cnt +=1
print(cnt)