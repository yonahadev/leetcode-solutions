class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = []
        suffixProducts = []
        prefix = 1
        for idx,value in enumerate(nums):
            prefixProducts.append(prefix)
            prefix *= value
        print(prefixProducts)
        suffix = 1
        for idx,value in enumerate(reversed(nums)):
            suffixProducts.append(suffix)
            suffix *= value
        print(suffixProducts)
        output = []
        for i in range(len(nums)):
            output.append(prefixProducts[i]*suffixProducts[len(nums)-i-1])
        return output
