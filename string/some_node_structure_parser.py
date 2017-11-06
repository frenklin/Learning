"""s = "[ 1 [ 2 ] [ 3 [ 4 ] [ 5 ] ] ]"; """


class Node:
    def __init__(self, leftNode, rightNode, value):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = value


def mkNode(val, lstL, lstR):
    return Node(val, parseNodes(lstL), parseNodes(lstR))

def findNodeEndIndex(lst):
    level = 0 
    for i in range(0, len(lst)):
        if lst[i] is '[':
            level+=1
        elif lst[i] is ']':
            level-=1
        if level is 0:
            return i
    print('Error')

def parseNodes(lst):
    for i in range(0, len(lst)):
        if lst[i] is '[':
            item = lst[i]    
            if item is "[":
                value=lst[1]
                leftNodeEndIndex=findNodeEndIndex(lst[2:])
                rightNodeEndIndex=findNodeEndIndex(lst[leftNodeEndIndex:])
            return mkNode(value, lst[2:leftNodeEndIndex], lst[leftNodeEndIndex+1, rightNodeEndIndex])
    
    

data = '[ 1 [ 2 ] [ 3 [ 4 ] [ 5 ] ] ]'
print(parseNodes(list(data.split(' '))))