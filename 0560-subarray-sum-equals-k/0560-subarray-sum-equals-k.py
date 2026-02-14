#this is way too hard for me
class Solution:
    '''def subarraySum(self, nums: List[int], k: int) -> int:
        # 1. Initialize your map with the "Base Case"
        # We've seen a sum of 0 exactly once (at the very beginning)
        prefix_counts = {0: 1}
        
        curr_sum = 0
        total_subarrays = 0
        
        for n in nums:
            # 2. Update the running sum
            curr_sum += n
            
            # 3. CHECK: Does (curr_sum - k) exist in our map?
            # If it does, add its count to total_subarrays
            diff = curr_sum - k
            if diff in prefix_counts:
                total_subarrays += prefix_counts[diff]
            
            # 4. UPDATE: Add the current curr_sum to the map
            # (Use .get() to handle sums we haven't seen before)
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            
        return total_subarrays
'''
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr_sum = 0
        stored_sums = {0:1}
        count = 0

        for n in nums: 
            curr_sum += n
            if curr_sum - k in stored_sums:
                count += stored_sums[curr_sum - k]
            stored_sums[curr_sum] = stored_sums.get(curr_sum, 0) + 1
        return count 

            