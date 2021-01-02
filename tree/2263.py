import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

tree = {}
left = []
right = []

rootNode = postorder.pop(-1)
index = inorder.index(rootNode)

left = postorder[:index]
right = postorder[index:]

tree[rootNode][1] = left.pop(-1)
tree[rootNode][0] = right.pop(-1)



