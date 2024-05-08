from typing import List


# 내 풀이
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [None] * len(score)

        for i in range(len(score)):
            max_index = score.index(max(score))
            if i == 0:
                s = "Gold Medal"
            elif i == 1:
                s = "Silver Medal"
            elif i == 2:
                s = "Bronze Medal"
            else:
                s = str(i + 1)
            result[max_index] = s
            score[max_index] = -1

        return result


# GPT 최적화 요청
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        result = [""] * len(score)

        for rank, (s, i) in enumerate(sorted_scores, 1):
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)

        return result


# 다른사람 풀이
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]


score, expected = [5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
score, expected = [10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
result = Solution().findRelativeRanks(score)
assert result == expected
