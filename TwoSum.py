class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given an array of integers nums and an integer target, return the indices i and j 
        such that nums[i] + nums[j] == target and i != j.
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j] #i will always be the smallest index

        #If not found, return a signal value
        print("No valid sums")
        return [-999, -999]
        