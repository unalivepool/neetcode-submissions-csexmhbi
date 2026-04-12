class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Execution summary
        #- 35 mins on first attempt
        #- concrete approach; syntax issues;
        #- got lost moving from binary search to 2 sum

        result=[]
        nums.sort()# O(nlogn) - sort the array first
        for i in range(0, len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: #skip repeat triplet
                continue
            
            l, r= i+1, len(nums)-1
            while l<r:
                total= nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                elif total==0:
                    result.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return result




