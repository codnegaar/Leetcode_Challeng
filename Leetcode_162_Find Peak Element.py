'''

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
          Input: nums = [1,2,3,1]
          Output: 2
          Explanation: 3 is a peak element and your function should return the index number 2.
          
Example 2:
        Input: nums = [1,2,1,3,5,6,4]
        Output: 5
        Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
        
Constraints:
        1 <= nums.length <= 1000
        -231 <= nums[i] <= 231 - 1
        nums[i] != nums[i + 1] for all valid i

'''

# Python solution

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
      
      
# Python 3 solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
                
        if nums[end] > nums[start]:
            return end
        
        return start

# solution 4
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-2147483649)
        nums.insert(0,-2147483649)
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i-1
                break
            else:
                continue
