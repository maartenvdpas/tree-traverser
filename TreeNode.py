class TreeNode:
    REPRESENTATION_STRING = "val={0}, children=[{1}]"

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        child_represenation = ",".join(str(child) for child in self.children)
        return TreeNode.REPRESENTATION_STRING.format(self.value, child_represenation)

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def getSize(self):
        childrenSize = 0
        for child in self.children:
            childrenSize += child.getSize()
        return childrenSize + 1
