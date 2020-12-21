# 내가 작성한 코드
array = list(map(int,input().split(' ')))
if sorted(array) == array:
    print("ascending")
elif sorted(array,reverse=True) == array:
    print("descending")
else:
    print("mixed")

# 강의 코드 ( sorted라는 메소드를 활용하지 않음 )
a = list(map(int,input().split(' ')))
ascending = True
descending = True
for i in range(1,8):
    if a[i] > a[i - 1]:
        descending = False
    elif a[i] < a[i - 1]:
        ascending = False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

# 리뷰
# 파이썬 내장함수를 활용하지 않고도 로직을 구현할줄 알아야함.
