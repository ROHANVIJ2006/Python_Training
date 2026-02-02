nums=[0,1,0,3,12]
j = 0  # index for non-zero placement
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)