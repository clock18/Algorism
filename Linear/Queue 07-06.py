## 함수
def isQueueFull():
    global size, queue, front, rear
    if rear == size -1:
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front, rear
    if isQueueFull() :
        print('queue 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global size, queue, front, rear
    if front == rear :
        return True
    else:
        return False

def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print('queue 텅!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global size, queue, front, rear
    if isQueueEmpty():
        print('queue 텅!')
        return None
    return queue[front+1]



## 전역
size = 5
queue = [ None for _ in range(size) ]
front = rear = -1


## 메인
enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('선미')
# enQueue('재남')
# print('출구<===', queue, '<===입구')
# enQueue('아이유')

print('출구<===', queue, '<===입구')
print('밥 손님 : ',deQueue())
print('다음 손님 준비 : ',peek())
print('밥 손님 : ',deQueue())
print('출구<===', queue, '<===입구')
print('밥 손님 : ',deQueue())

