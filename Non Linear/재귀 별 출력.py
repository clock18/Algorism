## 함수
def star(num) :
    if num > 0:
        star(num-1)
        print('*'*num)


## 메인
star(5)