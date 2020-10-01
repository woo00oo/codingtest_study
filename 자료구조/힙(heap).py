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
    #삽입
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

    def move_down(self,poped_idx):
        left_child_popped_idx = poped_idx*2
        right_child_popped_idx = poped_idx*2+1

        # 왼쪽 자식노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        #오른쪽 자식 노드만 없을때 (왼쪽 자식 노드는 있음) => 완전 이진트리이기 때문
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False

        #왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                    return  True
                else:
                    return False



    #삭제
    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1] #마지막 노드를 루트 노드로 옮겨줌
        del self.heap_array[-1]
        poped_idx = 1
        while self.move_down(poped_idx):
            left_child_popped_idx = poped_idx * 2
            right_child_popped_idx = poped_idx * 2 + 1

            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_popped_idx

            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx],self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx

        return returned_data







