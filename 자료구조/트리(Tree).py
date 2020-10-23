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

        ######case1 : 삭제할 노드가 단말 노드일 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value <self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        #####case2 : 삭제할 Node가 자식노드를 한 개 가지고 있을 경우

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

        #####case3 : 삭제할 Node가 자식노드를 2개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right != None:
            #삭제할 노드가 부모노드의 왼쪽에 있을 경우
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.current_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            #삭제할 노드가 부모노드의 오른쪽에 있을 경우
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.current_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right



#0-999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0,999))

#선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500으로 생성
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

#입력한 100개의 숫자 검색(검색 기능확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search failed',num)

#입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0,99)])
#선택한 10개의 숫자를 삭제(삭제기능확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delet failed',num)
