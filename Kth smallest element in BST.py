class Solution:
    def collectInOrderTraversal(self,root,arr):
        if root==None:
            return
        self.collectInOrderTraversal(root.left,arr)
        arr.append(root.data)
        self.collectInOrderTraversal(root.right,arr)
    def kthSmallest(self,root,k):
        arr=[]
        self.collectInOrderTraversal(root,arr)
        n=len(arr)
        if n<K:
            return -1
        return arr[k-1]