class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStringToStrs={}
        for s in strs:
            key = "".join(sorted(s)) # sorted: Return a new sorted list from the items in iterable
            if key not in sortedStringToStrs:  # You can simplify the "check if key exists" logic using collections.defaultdict. defaultdict(list) It removes the need for the if/else block entirely.
                sortedStringToStrs[key]=[]
            sortedStringToStrs[key].append(s)

        
        return list(sortedStringToStrs.values())