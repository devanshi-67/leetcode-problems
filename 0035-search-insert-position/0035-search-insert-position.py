class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                i += 1

        if target not in nums:
            nums.append(target)
            for i in range(len(nums)):
                if nums[i] >= target:
                    nums.insert(i,target)
                    return i
            
        