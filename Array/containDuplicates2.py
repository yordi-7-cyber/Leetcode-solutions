class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i  
        return False
sol = Solution()
nums = [1,2,3,1,2,3]
k = 2
result = sol.containsNearbyDuplicate(nums, k)
print(result)  