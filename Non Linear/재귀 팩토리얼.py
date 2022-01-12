## 함수
def mulNumber(num) :
    if num <= 1 :
        return 1
    return num * mulNumber(num-1)


## 메인
print(mulNumber(10))