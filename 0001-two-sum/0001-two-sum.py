class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of the numbers we have seen so far
        seen = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in seen:
                return [seen[complement], i]
            
            # If not, store the number and its index
            seen[num] = i