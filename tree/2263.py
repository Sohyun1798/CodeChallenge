import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

tree = {}

io_left = []
io_right = []

po_left = []
po_right = []

rootNode = postorder.pop(-1)
index = inorder.index(rootNode)

po_left = postorder[:index]
po_right = postorder[index:]

io_left = inorder[:index]
io_right = inorder[index+1:]

tree[rootNode][1] = po_left.pop(-1)
tree[rootNode][0] = po_right.pop(-1)



