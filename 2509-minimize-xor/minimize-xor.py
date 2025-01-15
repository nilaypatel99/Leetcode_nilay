class Solution:
    def isSet(self, x, bit):
        return (x & (1 << bit)) != 0

    def setBit(self, x, bit):
        return x | (1 << bit)

    def unsetBit(self, x, bit):
        return x & ~(1 << bit)

    def minimizeXor(self, num1, num2):
        x = num1
        requiredSetBitCount = bin(num2).count('1')
        currSetBitCount = bin(x).count('1')

        bit = 0
        if currSetBitCount < requiredSetBitCount:
            while currSetBitCount < requiredSetBitCount:
                if not self.isSet(x, bit):
                    x = self.setBit(x, bit)
                    currSetBitCount += 1
                bit += 1
        elif currSetBitCount > requiredSetBitCount:
            while currSetBitCount > requiredSetBitCount:
                if self.isSet(x, bit):
                    x = self.unsetBit(x, bit)
                    currSetBitCount -= 1
                bit += 1

        return x


