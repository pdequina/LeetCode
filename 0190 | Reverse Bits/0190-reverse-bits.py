class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse = 0
        for i in range(32):
            reverse = reverse << 1
            if n & 1:
                reverse = reverse ^ 1
            n = n >> 1
        return reverse
