class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive O(n^2): for each index, multiply all elements except itself.
        # res = []
        # for i in range(0, len(nums)):
        #     prod = 1
        #     for j in range(0, len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     res.append(prod)

        # return res


        # Divsion appraoch: 
        # If we know the product of all non-zero numbers, we can easily compute the answer for each position using division — as long as there are no division-by-zero issues.

        # So we first check how many zeros the array has:

        # If there are two or more zeros, then every product will include at least one zero → the entire res is all zeros.
        # If there is exactly one zero, then only the position containing that zero will get the product of all non-zero numbers. All other positions become 0.
        # If there are no zeros, we can safely do:
        # result[i] = total_product // nums[i]

        # prod = 1
        # zero_count = 0
        # for num in nums:
        #     if num == 0:
        #         zero_count = zero_count +1
        #     else:
        #         prod*=num
        
        # # 2 or more zeros
        # if zero_count > 1:
        #     return [0] * len(nums)
        
        # # one zero
        # res = [0] * len(nums)
        # i = 0
        # if zero_count == 1 :
        #     for num in nums:
        #         if num == 0:
        #             res[i] = prod
        #             return res
        #         i = i +1

        # # 0 zeros...
        # i = 0
        # for num in nums:
        #     res[i] = prod // num
        #     i = i +1
        # return res


        # Prefix & Suffix appraoch
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

            
        



