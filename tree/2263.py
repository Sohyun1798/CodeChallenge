import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

in_location = [0]*(n+1)

for i in range(n):
    in_location[inorder[i]] = i

tree = [[0,0] for _ in range(n+1)]

def find_tree(in_left, in_right, post_left, post_right):

    if post_left <= post_right:
        parents = postorder[post_right]
        post_index = in_location[parents]
        
        left_count = post_index - in_left
        
        if left_count > 0:
            tree[parents][0] = postorder[post_left+left_count-1]
    
        right_count = in_right - post_index

        if right_count > 0:
            tree[parents][1] = postorder[post_right-1]

        find_tree(in_left, post_index-1, post_left, post_left+left_count-1)
        find_tree(post_index+1, in_right, post_right-right_count, post_right-1)

find_tree(0, n-1, 0, n-1)

def pre_order(start):

    print(start, end=" ")
   
    if tree[start][0] != 0:
        pre_order(tree[start][0])
    if tree[start][1] != 0:
        pre_order(tree[start][1])

pre_order(postorder[-1])