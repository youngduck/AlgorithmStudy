n=int(input())
tree=['.','A']+['.']*10000000


for i in range(n):    
    node,left,right=input().split()
    find=tree.index(node)
    tree[find]=node
    tree[find*2]=left
    tree[find*2+1]=right

#전위순회
def DLR(node):
    print(tree[node],end='')
    if tree[node*2] != '.':
        DLR(node*2)
    if tree[node*2+1] != '.':
        DLR(node*2+1)

#중위순회
def LDR(node):
    if tree[node*2] != '.':
        LDR(node*2)
    print(tree[node],end='')
    if tree[node*2+1] != '.':
        LDR(node*2+1)
#후위순회
def RLD(node):
    if tree[node*2] != '.':
        RLD(node*2)
    if tree[node*2+1] != '.':
        RLD(node*2+1)
    print(tree[node],end='')

DLR(1)
print('')
LDR(1)
print('')
RLD(1)
