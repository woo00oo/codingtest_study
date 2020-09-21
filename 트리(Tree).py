class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else :
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

    def delete(self,value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        #case1 : 삭제할 노드가 단말 노드일 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value <self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        #case2 : 삭제할 Node가 자식노드를 한 개 가지고 있을 경우

        #삭제할 노드의 자식노드가 왼쪽에 있을 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        #삭제할 노드의 자식노드가 오른쪽에 있을 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right