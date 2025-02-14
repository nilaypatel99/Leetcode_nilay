class ProductOfNumbers:
    def __init__(self):
        self.prefixProduct = [1]  # Prefix product list (1-based indexing)

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]  # Reset if zero is encountered
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixProduct):  # If k exceeds available numbers due to reset
            return 0
        return self.prefixProduct[-1] // self.prefixProduct[-(k+1)]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)