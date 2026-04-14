class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} # number -> freq
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        arr = [] # ([freq, number])
        for num,freq in hashMap.items():
            arr.append([freq,num])
        
        arr.sort() # sort based on freq

        res = []
        for i in range(k):
            res.append(arr.pop()[1]) # we want num, not freq

        return res