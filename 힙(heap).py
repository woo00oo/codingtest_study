class Heap:
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        if(inserted_idx <= 1): #루트노드일 경우
            return False

        parent_idx = inserted_idx //2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):

        #힙에 새로운 데이터 값을 넣어줌
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        # 힙의 형태로 바꾸어줌 (최대힙 & 최소힙)
        inserted_idx = len(self.heap_array) -1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx //2 #부모 노드를 알아냄
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True




