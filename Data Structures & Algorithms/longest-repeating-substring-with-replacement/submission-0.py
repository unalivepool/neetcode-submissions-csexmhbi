class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right=0,0
        n=len(s)
        longest_len=0
        freq={}
        while right<n: #extend right
            freq[s[right]]=freq.get(s[right],0)+1 #add right
            #check validity
            window_len=right-left+1
            max_freq=max(freq.values())
            
            is_valid=window_len-max_freq<=k
            #if invalid            
            while not is_valid: #shrink left
                freq[s[left]]=freq.get(s[left])-1 #remove left
                left+=1 #move_left
                
                window_len=right-left+1 #update answer
                max_freq=max(freq.values())
                is_valid=window_len-max_freq<=k
            longest_len=max(longest_len,window_len)
            right+=1
        return longest_len
            

                


        