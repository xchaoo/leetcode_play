class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        hint : DFS 遍历生成, l,r =0保证 n对括号
        """
    def helpler(self, l, r, item, res):
        if l>r:
            return
        if l==0 and r==0:
            res.append(item)
        if l>0:
            self.helpler( l-1, r, item + '(', res)
        if r>0:
            self.helpler( l, r-1, item + ')', res)
    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res