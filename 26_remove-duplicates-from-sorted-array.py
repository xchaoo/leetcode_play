class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        hint : 双指针, 对比前后字符是否一致。
        """
        if nums==[]:
            return 0
        index=0
        for i in range(1,len(nums)):
            if nums[index] !=  nums[i]:
                index+=1
                nums[index] = nums[i]
        return index+1