class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class NodeMgn:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next현

    def delete(self,data):
        if self.head == '':
            print("데이터가 존재하지 않습니다.")
            return
        if self.head.data == data: #첫번째 노드 삭제일 경
            temp = self.head
            self.head = self.head.next
            del temp
        else: #중간, 마지막 노드 삭제일 경
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next



linkedlist1 = NodeMgn(0)
#linkedlist1.desc()

for i in range(1,10):
    linkedlist1.add(i)

linkedlist1.desc()