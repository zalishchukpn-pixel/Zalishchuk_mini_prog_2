class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Extract the last bit of n
            bit = n & 1

            # Shift result to the left to make space for the extracted bit
            result = (result << 1) | bit

            # Shift n to the right to process the next bit
            n = n >> 1

        return result
    
