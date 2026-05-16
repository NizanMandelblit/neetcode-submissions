class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor = addition without carry
        # &<<1 = carry

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        # 0x7FFFFFFF is the max positive value for a signed 32-bit int (0111...1111).
        # If 'a' is less than or equal to this, it's a positive number.
        # If 'a' is greater, the 32nd bit is 1, meaning it represents a negative number.
        # ~(a ^ mask) converts that unsigned 32-bit value back into Python's native negative format.
        return a if a <= max_int else ~(a ^ mask)