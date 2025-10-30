class Solution:
    def smallestNumber(self, n: int) -> int:
        #get the binary representation and then set the bits to 1
        num_bits = n.bit_length()
        y = (1<<num_bits)-1
        res = n | y
        return res

