## 함수
def isStackFull() :
    global size, stack, top
    if top == size - 1 :
        return True
    else:
        return False

def push(data) :                    # 스텍이 꽉찼는지 확인
    global size, stack, top         # 꽉 찬 상태라면 오버플로우 발생
    if isStackFull() :              # 함수자체가 true, false 임
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global size, stack, top
    if top == -1 :
        return True
    else:
        return False

def pop() :                 # 맨 위에것부터 추출
    global size, stack, top
    if isStackEmpty() :
        print('스택이 비었습니다')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global size, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return
    return stack[top]


## 전역
size = 5
stack = [ None for _ in range(size) ]      # list comprehension
top = -1


## 메인
push('커피1')
push('커피2')
# push('커피3')
# push('커피4')
# push('커피5')
print(stack)
# push('커피6')
print('다음예정 : ',peek())

retData = pop()
print(retData)
retData = pop()
print(retData)
retData = pop()
print(retData)

print(stack)