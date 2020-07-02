# n : 배열의 크기
# S : 배열
# x : 찾고자 하는 수
# location : 찾고자 하는 수의 위치

def seqsearch(n, S, x):
    location = 0
    while location <= n and S[location] != x:
        location = location + 1
    if location > n:
        location = 0
    return location 

S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
x = 8

seq = seqsearch(n, S, x)

print(seq)

