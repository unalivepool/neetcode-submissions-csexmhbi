class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} 
        for i,x in enumerate(nums):
            y= target - nums[i]
            if y in seen:
                return [seen[y],i]
            seen[x]=i

        # nums.sort() #prev apporach
        # for i,val in enumerate(nums):
        #     j =next((j for j,x in enumerate(nums) if x==(target-nums[i]) and j!=i), -1)
        #     if j!=-1:
        #         return [i,j]


#=============
#
#Scratchpad
# [7,3,3,5,0,-1,2] - target=4 (5+-1),  [3,5]
# ~1000 elements
#brute force =  
# for i in nums:
#   for j in nums:
#       if nums[i]+nums[j]==target
#            return i,j
#
#7, move to 3, check if 7+3==target, if not , move to next.
#   move to 3, skip
#7, +5, # will sorting help? 
# nlogn for sorting. - not very much if -ve numbers!
# for every element in conisderation, check if target-i is present.
# for 7, search for 3 
#  so sort the array-  nlogn, the search using binary search.
#   nlogn + logn = nlogn time
#  space complexity when sorting, and when binary searching.
# nums.sort() #nlogn
# for i, val in enumerate(nums):
#  k=target-val
#  j=nums.index(k) # logn time
#   if j !=-1:
#       return i,j
# [7,3,3,5,0,-1,2] ; target=4
# i=0,val=7, k=4-7 = -3,; j=-1 
# i=1,val=3, k=4-3=1 ; j=-1
# i=2,val=3, k=4-3=1,; j=-1
# i=3,val=5, k=4-5=-1; j=5 ;3,5
#
#
# alternative approach


# lets do the 2 pointer approach
# sort the array!, 