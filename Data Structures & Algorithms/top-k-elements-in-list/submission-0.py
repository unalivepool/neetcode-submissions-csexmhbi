class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counts=defaultdict(int)
        for e in nums:
            counts[e]+=1
        return list(dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]).keys())
