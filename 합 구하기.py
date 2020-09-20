n =int(input())

# O(n)
def int_sum (n):
    sum = 0
    for index in range(1,n+1):
        sum += index
    return sum

#O(1)
#시간 복잡도가 더 빠른 알고리즘.
def sum_all(n):
    return int(n*(n+1)/2)

