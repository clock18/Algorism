import random

## 함수
def selectionSort(ary) :
    n = len(ary)
    for cy in range(0, n-1) :       # 싸이클 수
        minIdx = cy
        for i in range(cy+1, n):    # 정렬 인원 수
            if ary[minIdx] > ary[i]:
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary


## 전역 변수
dataAry = [ random.randint(100,200) for _ in range(10) ]


## 메인 함수
print('정렬 전 ==>', dataAry)

dataAry = selectionSort(dataAry)

print('정렬 후 ==>', dataAry)

