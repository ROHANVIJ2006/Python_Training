class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Bubble sort - compare adjacent elements and swap if in wrong order
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]"""
        count0=count1=count2=0
        for v in nums:
            if v==0:
                count0+=1
            elif v==1:
                count1+=1
            else:
                count2+=1
        ind=0
        for _ in range(count0):
            nums[ind] = 0
            ind += 1

        # Fill 1s
        for _ in range(count1):
            nums[ind] = 1
            ind += 1

        # Fill 2s
        for _ in range(count2):
            nums[ind] = 2
            ind += 1

        """
        Do not return anything, modify nums in-place instead.
        """