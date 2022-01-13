import random

## 정의
def arySum(ary,num):
    if num <= 0 :
        return ary[0]
    return arySum(ary,num-1) + ary[num]


## 전역
ary = [random.randint(10,90) for _ in range(random.randint(10,20))]


## 메인
print(ary)
print(arySum(ary,len(ary)-1))