class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for s in strs:
            key=''.join(sorted(s)) # assuming quick sort, O(nlogn)- time, and O(1) space; O(n) space, worst case
            # if key in group.keys(): # O(1)
            group.setdefault(key,[]).append(s)
            # else:
            #     group.setdefault()
        return [x for x in group.values()]

        