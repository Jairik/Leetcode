class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' Problem:
        Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
        '''
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
    
    #True Solutions: Although this works, more efficiency may be acheived by loading all sets into a hashmap
