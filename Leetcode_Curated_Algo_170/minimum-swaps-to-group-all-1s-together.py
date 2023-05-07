class Solution:
    def minSwaps(self, data):
        sizeOfWindow = sum(data)
        zeros = minSwaps = len(data[:sizeOfWindow]) - sum(data[:sizeOfWindow])

        l,r = 0,sizeOfWindow

        while r<len(data):
            
            if data[l] == 0:
                zeros -= 1

            if data[r] == 0:
                zeros += 1

            minSwaps = min(minSwaps, zeros)
            l += 1
            r += 1

        return minSwaps
