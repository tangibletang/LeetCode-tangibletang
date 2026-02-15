class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high: #test this condition later
            mid = (low + high) // 2
            #condition 0: It is mid 
            if nums[mid] == target: 
                return mid
            #condition 1: the "normal" side is on the left of middle  
            if nums [low] <= nums[mid]:  
                if target < nums[mid] and target >= nums[low]: #target is on the normal side
                    high = mid -1 
                else: #target <low 
                    low = mid + 1
            else:# nums [mid] < nums [high]: "normal" side is on the right
                if target > nums[mid] and target <= nums[high]: 
                    low = mid + 1
                else: #target now in the normal side
                    high = mid - 1
            
        print (low, mid, high)
        return -1