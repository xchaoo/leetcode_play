class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        
        hint : 数学 - 如何筛选质数 - 埃拉托斯特尼筛法，遍历<n的n**0.5的倍数   
        """        
        if n <= 2:
            return 0
        f_lis = [False] * n
        for i in range(2, int(n**0.5)+1):
            if f_lis[i]:
                continue
            j = i 
            while j*i<n:
                f_lis[j*i] = True
                j+=1
        ans = 0
        #for i in f_lis:
        #    if not i: ans+=1
        for i in range(2, n):
            if not f_lis[i]: ans += 1
        return ans