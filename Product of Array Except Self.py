'''class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans'''

nums = [1, 2, 3, 4]
ans = [1, 1, 1, 1]
su = 1

# First pass: calculate prefix products (left to right)
for i in range(len(nums)):
    ans[i] = su
    su *= nums[i]

# Reset su for suffix products
su = 1

# Second pass: multiply with suffix products (right to left)
for j in range(len(nums)-1, -1, -1):
    ans[j] *= su
    su *= nums[j]

print(ans)  # Output: [24, 12, 8, 6]