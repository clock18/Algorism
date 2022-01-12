import random

## 함수
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end :
        mid = (start + end) // 2
        if dataAry[mid] == fData :
            return mid
        elif dataAry[mid] < fData :
            start = mid + 1
        else :
            end = mid - 1

    return pos


## 전역
size = 10
dataAry = [ random.randint(1,99) for _ in range(size) ]
findData = dataAry[random.randint(0,size-1)]
dataAry.sort()

## 메인
print('배열==>', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(findData, '없어요')
else :
    print(findData, '가', position, ' 에 있음')