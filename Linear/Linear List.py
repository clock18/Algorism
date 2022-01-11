# 파이썬에서는 배열이라고 부르고, 자료구조에서는 리스트라고 부른다
# 시계열 데이터 (시간순서로 생성되는 데이터)에 주로 사용 : 신문의 날짜별 기사

## 함수 선언부
def add_data(friend):       # 데이터 연속으로 추가
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(order, friend):     # 특정 인덱스에 데이터 추가
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, order, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[order] = friend

def delete_data(position):      # 인덱스 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    for i in range(position + 1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])


## 전역 변수부
katok = []
select = -1


# 메인 코드부
if __name__ == "__main__":

    while (select != 4):

        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(katok)
        elif (select == 2):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(katok)
        elif (select == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(katok)
        elif (select == 4):
            print(katok)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
