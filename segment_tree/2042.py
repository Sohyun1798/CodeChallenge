import sys
input = sys.stdin.readline

def init(node, start, end):
    print("node:", node, "start:", start, "end:", end)
    print("tree:", tree)
    if start == end:
        print("start and end", start)
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

n, m,k = map(int, input().rstrip().split())

l = []
tree = [0] * 30

for _ in range(n):
    l.append(int(input().rstrip()))

init(1,0,n-1)

print(tree)