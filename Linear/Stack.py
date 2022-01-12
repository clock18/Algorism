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
print('push끝낸후:',stack)

# POP
data = stack[top]
stack[top] = None
top -= 1
print(data)
print('꿀물을빼고난후:',stack)

data = stack[top]
stack[top] = None
top -= 1
print(data)
print('녹차를뺴고난후:',stack)

data = stack[top]
stack[top] = None
top -= 1
print(data)
print('커피를빼고난후:',stack)