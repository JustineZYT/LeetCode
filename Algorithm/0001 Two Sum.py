class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re=[]
        s=set(nums)
        for i in range(len(nums)):
            a=target-nums[i]
            if (a in s) and nums.index(a)!=i:
                b=nums.index(a)
                re.append(i)
                re.append(b)
                break
        return re