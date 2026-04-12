class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        seen=defaultdict(int)
        if len(s)!=len(t):
            return False
        i,j=0,0
        while i<len(s) and  j<len(t):
            seen[s[i]]+=1
            seen[t[j]]-=1
            i+=1
            j+=1
            # print(seen)
        for c in seen.keys():
            if seen[c]!=0:
                return False
        return True


        # for c in s:
        #     seen[c]+=1
        # for c in t:
        #     seen[c]-=1
        # for c in seen.keys():
        #     if c!=0:
        #         return False
        # return True

# anagrams of each other; 
#if the lengts are different, return false
# count the number of instances for each character
# o(k) space-disticnt letters, o(l) time (length of string)
# for each c in s: ; 
#   seen[c]+=1
# for each c in t:
#   seen[c]-=1
# for each c in seen:
#   if c!=0:
#.     retrurn False
# retrun True