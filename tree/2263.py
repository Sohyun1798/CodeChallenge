import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

tree = {}
root_node = postorder[-1]

tree[root_node][1] = postorder[-2]