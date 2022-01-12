## 함수

def pow(x,n) :

    if n == 0 :
        return 1
    return x * pow(x, n-1)

## 메인

print('답 ==>', pow(2,4))