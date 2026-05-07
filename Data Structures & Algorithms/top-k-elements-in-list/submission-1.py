from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        arr = []

        for key,val in cnt.items():
            arr.append([val,key])
        
        arr.sort()
        res= []
        while k>0:
            res.append(arr.pop()[1])
            k-=1
        
        return res

        