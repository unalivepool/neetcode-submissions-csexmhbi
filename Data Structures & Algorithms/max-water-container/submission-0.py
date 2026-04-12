class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #21 minutes to think; could not arrive at the condition on when to move 2 pointers
        i,j=0,len(heights)-1
        max_area=-1
        while i<j:
            curr_area= (j-i) * min(heights[j],heights[i])
            if curr_area> max_area:
                max_area=curr_area
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_area