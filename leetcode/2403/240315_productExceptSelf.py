# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# 내가 처음에 풀었던 풀이 (시간초과)
# class Solution:
#     def multiply_array(self, arr):
#         result = 1
#         for num in arr:
#             result *= num
#         return result

#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         answer = []
#         for i in range(len(nums)):
#             copy = nums.copy()
#             copy.pop(i)
#             tmp = self.multiply_array(copy)
#             answer.append(tmp)
#         return answer


# GPT 가 최적화해준 코드 시간복잡도 O(N^2) 에서 O(N) 으로 변경됨
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # 왼쪽에서부터 각 요소의 곱 계산
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        # 오른쪽에서부터 각 요소의 곱 계산
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
