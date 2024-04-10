# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from typing import List


#########################################################################################
# 풀이1 : Queue 를 이용한 시뮬레이션
#########################################################################################
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = []

        for card in sorted(deck, reverse=True):  # 1단계: 정렬된 덱을 역순으로 반복합니다.
            if result:  # 2단계: 결과 리스트가 비어 있지 않다면
                result.insert(0, result.pop())  # 3단계: 마지막 요소를 처음으로 이동합니다.
            result.insert(0, card)  # 4단계: 현재 카드를 결과 리스트의 처음에 삽입합니다.

        return result


#########################################################################################
# 풀이2 : 투포인터를 사용한 풀이 (더 성능이 좋다.)
#########################################################################################
# class Solution:
#     def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
#         N = len(deck)
#         result = [0] * N
#         skip = False
#         index_in_deck = 0
#         index_in_result = 0

#         deck.sort()

#         while index_in_deck < N:
#             # There is an available gap in result
#             if result[index_in_result] == 0:

#                 # Add a card to result
#                 if not skip:
#                     result[index_in_result] = deck[index_in_deck]
#                     index_in_deck += 1

#                 # Toggle skip to alternate between adding and skipping cards
#                 skip = not skip

#             # Progress to the next index of result array
#             index_in_result = (index_in_result + 1) % N

#         return result


# 함수 테스트
deck_expected = [
    ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7]),
    ([1, 1000], [1, 1000]),
    ([1], [1]),
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, 6], [1, 4, 2, 6, 3, 5]),
    ([1, 2, 3, 4], [1, 3, 2, 4]),
]

for deck, expected in deck_expected:
    result = Solution().deckRevealedIncreasing(deck)
    assert result == expected
