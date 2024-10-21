class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res=0
        def dfs(root):
            if not root:
                return 0,0
            val1,num1=dfs(root.left)
            val2,num2=dfs(root.right)
            val=root.val+val1+val2
            num=1+num1+num2
            avg=val/num
            self.res=max(avg,self.res)
            return val,num
        
        dfs(root)
        return self.res
