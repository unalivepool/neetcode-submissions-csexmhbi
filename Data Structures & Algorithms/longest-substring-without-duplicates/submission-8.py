class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #16 mins to think; did not get the moving condition; 
        l=0
        max_length=0
        seen=set()

        for ch in s:
            while ch in seen:
                seen.remove(s[l])
                l+=1
            seen.add(ch)
            max_length=max(max_length,len(seen))
        return max_length
