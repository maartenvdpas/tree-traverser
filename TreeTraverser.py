from TreeNode import TreeNode
import random

def generateRandomTree(branchSize, treeDepth, minValue, maxValue):
    baseNode = TreeNode(randomValue(minValue, maxValue))
    
    if treeDepth > 0:
        for node in range(branchSize):
            baseNode.addChild(generateRandomTree(branchSize, treeDepth-1, minValue, maxValue))
    
    return baseNode

def randomValue(minValue, maxValue):
    return random.random() * (maxValue - minValue) + minValue

if __name__ == "__main__":
    tree = generateRandomTree(branchSize=2, treeDepth=10, minValue=0, maxValue=5)

    print(tree.getSize())
