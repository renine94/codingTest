# https://leetcode.com/problems/trapping-rain-water/submissions/1230144074/
# 2-pointer 방식으로 문제해결

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 높이 리스트가 비어 있는지 확인
        if not height:
            return 0

        # 포인터와 변수 초기화
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        # 두 포인터 접근 방식
        while left < right:
            # 왼쪽 포인터의 높이가 오른쪽 포인터의 높이보다 작은 경우
            if height[left] < height[right]:
                # 필요한 경우 left_max 업데이트
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # 갇힌 물을 계산하고 water 변수에 추가
                    water += left_max - height[left]
                # 왼쪽 포인터를 오른쪽으로 이동
                left += 1
            else:
                # 오른쪽 포인터의 높이가 왼쪽 포인터의 높이보다 작거나 같은 경우
                # 필요한 경우 right_max 업데이트
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # 갇힌 물을 계산하고 water 변수에 추가
                    water += right_max - height[right]
                # 오른쪽 포인터를 왼쪽으로 이동
                right -= 1

        # 총 갇힌 물을 반환
        return water


height_expected = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
]

for height, expected in height_expected:
    result = Solution().trap(height)
    assert result == expected
