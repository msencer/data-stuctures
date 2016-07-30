'''
This is a basic binary tree implementation
'''
from collections import deque

def isEqual(t1,t2):
    if t1 == None or t2 == None:
        return t1 == t2
    return t1.val == t2.val and isEqual(t1.left,t2.left) and isEqual(t1.right,t2.right)
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def __call__(self,left=None,right=None):
        self.left = left
        self.right = right
        return self
    def levelorder(self):
        '''
            Returns level-order representation of the binary tree in an array
        '''
        q = deque()
        q.append(self)
        res = []
        while q:
            n = q.popleft()
            res.append(n.val)
            if n.left!=None:
                q.append(n.left)
            if n.right!=None:
                q.append(n.right)
        return res

    def inorder(self):
        '''
            Returns in-order representation of the binary tree in an array
        '''
        if not self:
            return []
        res = []
        if self.left:
            res+=self.left.inorder()
        res += [self.val]
        if self.right:
            res+=self.right.inorder()
        return res
    def preorder(self):
        '''
            Returns pre-order representation of the binary tree in an array
        '''
        if not self:
            return []
        res = [self.val]
        if self.left:
            res+=self.left.preorder()
        if self.right:
            res+=self.right.preorder()
        return res
    def postorder(self):
        '''
            Returns post-order representation of the binary tree in an array
        '''
        if not self:
            return []
        res = []
        if self.left:
            res+=self.left.postorder()
        if self.right:
            res+=self.right.postorder()
        res += [self.val]
        return res
    def __repr__(self):
        return str(self.val)

if __name__ == "__main__":
    '''
                2
            3       4
        5        6     7
    '''
    t1 = TreeNode(2)(TreeNode(3)(TreeNode(5)),TreeNode(4)(TreeNode(6),TreeNode(7)))
    t2 = TreeNode(2)(TreeNode(3)(TreeNode(5)),TreeNode(4)(TreeNode(6),TreeNode(7)))
    assert isEqual(t1,t2)
    assert [2,3,4,5,6,7] == t1.levelorder()
    assert [5,3,2,6,4,7] == t1.inorder()
    assert [5,3,6,7,4,2] == t1.postorder()
    assert [2,3,5,4,6,7] == t1.preorder()
