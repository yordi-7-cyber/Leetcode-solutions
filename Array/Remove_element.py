class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[total]=nums[i]
                total+=1
        return total
nums=[3,2,2,3]        
val=3
sol=Solution()
new=sol.removeElement(nums,val)
print(new)
        