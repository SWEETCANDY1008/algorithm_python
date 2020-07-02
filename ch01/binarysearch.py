# n : 배열의 크기
# S : 배열
# x : 찾고자 하는 수
# location : 찾고자 하는 수의 위치

def binsearch(n, S, x):
    low = 0
    high = n
    location = 0

    while low <= high and location == 0:
        mid = (low + high) // 2             # / 대신 //을 사용하는 이유는 소수점을 자동으로 버려주기 때문
        if (x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return location
        

S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
x = 8

print(binsearch(n, S, x))


