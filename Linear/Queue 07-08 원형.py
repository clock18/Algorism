## 함수
def isQueueFull():
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front, rear
    if isQueueFull() :
        print('queue 꽉!')
        return
    rear = (rear + 1) % size
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
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global size, queue, front, rear
    if isQueueEmpty():
        print('queue 텅!')
        return None
    return queue[(front + 1) % size]

## 전역
size = 5
queue = [None for _ in range(size)]
front = rear = 0



## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('선미')
enQueue('재남')
print('출구<===', queue, '<===입구')
print('밥 손님 : ',deQueue())
print('밥 손님 : ',deQueue())
print('출구<===', queue, '<===입구')
enQueue('아이유')
print('출구<===', queue, '<===입구')
enQueue('재남')
print('출구<===', queue, '<===입구')