## 함수


## 전역
size = 5
stack = [ None for _ in range(size) ]      # list comprehension
top = -1



## 메인

# PUSH
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack)

# POP
data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)