## 함수
class Graph() :
    def __init__(self, size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

# print(list([0 for _ in range(4)] for _ in range(4)))
# ==> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


## 전역 변수
G = None



## 메인 코드
G = Graph(4)


for row in range(4):
    for col in range(4):
        print(G.graph[row][col], end='  ')
    print()