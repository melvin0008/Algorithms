def BinaryTree(s):
    return [s,[],[]]
    
def insertLeft(root,s):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[s,t,[]])
    else:
        root.insert(1,[s,[],[]])
    return root
        
def insertRight(root,s):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[s,[],t])
    else:
        root.insert(2,[s,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

x = BinaryTree('a')
insertLeft(x,'b')
insertRight(x,'c')
insertRight(getLeftChild(x),'d')
insertLeft(getRightChild(x),'e')
insertRight(getRightChild(x),'f')
print x        
