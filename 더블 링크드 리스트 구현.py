class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt :
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self,data):
        if self.head == None:
            return False

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False
#
    def insert_before(self,data,before_data):
        if self.head == None: #링크드 리스트가 비어있을 경우 맨 처음에 데이터 삽
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data: #특정 데이터를 찾음 (링크드 리스트의 데이터가 before_data랑 같을 경우 반복문을 빠져나옴)
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True