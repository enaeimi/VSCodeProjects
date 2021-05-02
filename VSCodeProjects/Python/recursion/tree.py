from typing import Any, List


class Tree:
    def __init__(self) -> None:
        self.call: str = ''
        self.returned: Any = None
        self.children: List[Tree] = []



def waysToClimb(n, prossibleSteps, tree):
    tree.call = 'waysToClimb('+ str(n)+')' #put changing parametere
    if n == 0:
        tree.returned = 1 #save the return value before return stm
        return 1
    else:
        nbWays = 0
        for steps in prossibleSteps:
            if(n-steps) >= 0:

                child = Tree()#create a new child for each recursive call 
                tree.children.append(child)
                nbWays += waysToClimb(n-steps, prossibleSteps, child)#pass the child as parameter 

        tree.returned = nbWays #save the return value before return stm
        return nbWays


def printTree(tree, indent=''):
    INDENT_SIZE = 4
    if tree is None or len(tree.children) == 0:
        print(tree.call + 'returned '+ str(tree.returned))
    else:
        print(tree.call + 'returned '+ str(tree.returned))
        for child in tree.children[:-1]:
            print(indent + '|' + '-' * INDENT_SIZE, end='')
            printTree(child,indent + '|' + ' ' * INDENT_SIZE)
        child = tree.children[-1]
        print(indent + 'L' + '-' * INDENT_SIZE, end='')
        printTree(child,indent + ' ' * INDENT_SIZE)


n = 10
possibleSteps = [2,4,5,8]
recursionTree = Tree()
waysToClimb(n,possibleSteps,recursionTree)
printTree(recursionTree)