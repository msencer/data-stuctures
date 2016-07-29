'''
This is a single-linkedlist implementation
'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __call__(self,node):
        self.appendRight(node)
        return self
    def __str__(self):
        '''
            Complexity of O(n)
        '''
        arr = []
        current = self
        while current:
            arr.append(str(current.val))
            current = current.next
        return ",".join(arr)
    def appendRight(self,node):
        '''
            Complexity of O(n)
        '''
        current = self
        while current.next!=None:
            current = current.next
        current.next = node
