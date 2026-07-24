from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L=[]
        s=[]
        counts=Counter(nums)
        count = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        for key in count:
            L.append(key)
        for i in range(k):
            s.append(L[i])
        return s

        