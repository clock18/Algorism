import random

## 함수
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1,len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx


## 전역 변수

testAry = [ random.randint(0,99) for _ in range(20)]


## 메인 코드
print(testAry)
minPos = findMinIndex(testAry)
print('최솟값==>', testAry[minPos])