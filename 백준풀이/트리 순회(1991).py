# 문제풀이:
#   트리를 구성하기 위해 class 사용

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preorder(node):
    print(node.value, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.value, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.value, end='')

N = int(input())
tree = dict()

for _ in range(N):
    node, left, right = input().split()
    tree[node] = Node(value=node, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
