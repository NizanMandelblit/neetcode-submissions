class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStringToStrs={}
        for str in strs:
            key = "".join(sorted(str))
            if key not in sortedStringToStrs:
                sortedStringToStrs[key]=[]
            sortedStringToStrs[key].append(str)

        
        return list(sortedStringToStrs.values())