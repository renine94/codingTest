from typing import List


###################################################################
# 내 풀이
###################################################################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result = 0

        boat = [0, 0]
        is_new_boat = False
        while people:

            if is_new_boat:
                boat = [0, 0]

            if len(people) == 1 and boat == [0, 0]:
                result += 1
                break

            weight = people.pop(0)

            boat[0] += weight
            boat[1] += 1

            if boat[0] < limit and boat[1] <= 2:
                is_new_boat = False
                if not people:
                    result += 1
                    break
                continue

            if boat[0] == limit and boat[1] == 2:
                is_new_boat = True
                result += 1
                continue
            else:
                result += 1
                is_new_boat = True
                people.insert(0, weight)
        return result


###################################################################
# GPT 최적화 풀이
###################################################################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 계수 정렬을 사용하여 people 리스트를 정렬
        counts = [0] * (limit + 1)
        for weight in people:
            counts[weight] += 1

        # 정렬된 people 리스트 재구성
        sorted_people = []
        for weight, count in enumerate(counts):
            sorted_people.extend([weight] * count)

        start, end = 0, len(sorted_people) - 1
        result = 0

        while start <= end:
            if sorted_people[start] + sorted_people[end] <= limit:
                start += 1
            end -= 1
            result += 1

        return result


###################################################################
# 다른사람 풀이
###################################################################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        2-pointer 알고리즘 사용
        """
        people.sort()
        boats = 0

        left, right = 0, len(people) - 1
        while left <= right:
            boats += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return boats


# people, limit, expected = [1, 2], 3, 1
people, limit, expected = [3, 5, 3, 4], 5, 4
# people, limit, expected = [5, 1, 4, 2], 6, 2
# people, limit, expected = [2, 2], 6, 1
result = Solution().numRescueBoats(people, limit)
assert result == expected
