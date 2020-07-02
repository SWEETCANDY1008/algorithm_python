# large_integer prod(large_integer u, large_integer v) {
#    large integer x, y, w, z
#    int n, m
   
#    n=maximum(u의 숫자 개수, v의 숫자 개수);
#    if(u==0 || v==0)
#       return 0;
#    else if(n <= threshold)
#       return 일반적인 방법으로 구한 u x v;
#    else {
#       m = n/2;
#       x = u divide 10^𝑚 y = u rem 10^𝑚
#       w = v divide 10^𝑚 z = v rem 10^𝑚
#       return prod(x, w) X 10^2𝑚 + (prod(w, y)) X 10^𝑚 + prod(y, z);
#    }
# } 

def maximum(first_len, second_len):
    if first_len > second_len:
        return first_len
    elif first_len < second_len:
        return second_len


def large_integer_prods(u, v):
    threshold = 48              # 컴퓨터가 일반적인 곱셈을 할 때 가장 효율적으로 계산하는 자리수의 길이. 그 이상 부터는 이 알고리즘이 효율적

    u_len = len(str(u))
    v_len = len(str(v))

    n = maximum(u_len, v_len)
    if u == 0 or v == 0:
        return 0
    elif n <= threshold:
        return u * v
    else:
        m = n // 2
        x = u // pow(10, m)
        y = u % pow(10, m)
        w = v // pow(10, m)
        z = v % pow(10, m)
        return large_integer_prods(x, w) * pow(10, 2*m) + (large_integer_prods(w, y)) * pow(10, m) + large_integer_prods(y, z);


print(large_integer_prods(123456789123456789123456789123456789123456789, 123456789123456789123456789123456789123456789))
