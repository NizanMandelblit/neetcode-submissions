class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        strs_sizes = [] #  store the sizes of each string
        res = ""
        for s in strs:
            strs_sizes.append(len(s))
        
        # Build a single string by:
        # Writing all sizes separated by commas.
        # Adding a '#' to mark the end of the size section.
        # Appending all the actual strings in order.
        for sz in strs_sizes:
            res += str(sz)
            res+= ','
        res+= '#'
        
        for s in strs:
            res+=s

        return res
         
        
        


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        # Read characters from the start until reaching '#' to extract all recorded sizes:
        # Parse each size by reading until a comma.
        # After the '#', extract substrings according to the sizes list:
        # For each size, read that many characters and append the substring to the result.
        # Return the list of decoded strings.
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur)) # covnert size str into a int
            i += 1
        i += 1 # skip the '#'
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res


# Time: O(m) for encode/decode
# Space: O(m+n) for encode/decode
# where m is the sum of lengths of all the strings
# and n is the number of strings.
        

