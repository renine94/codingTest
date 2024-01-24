# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solutions/4616637/python-dfs/?envType=daily-question&envId=2024-01-24


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        paths = []
        
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            path = path + [node.val]

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.right:
                    stack.append((node.right, path))
                if node.left:
                    stack.append((node.left, path))
        
        
        r = list(filter(self.check_palindrom, paths))
        return len(r)
        
    def is_palindrome(self, arr: list[int]):
        # 리스트의 원소들을 세서 각각의 개수를 저장하는 딕셔너리를 만듭니다.
        element_count = {}
        for element in arr:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        
        # 홀수 개수를 갖는 원소가 최대 하나까지만 허용됩니다.
        odd_count = 0
        for count in element_count.values():
            if count % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return False  # 홀수 개수를 갖는 원소가 두 개 이상이면 회문을 만들 수 없음
        
        return True
    
    def check_palindrom(self, nums):
        is_palindrom = 0
        for i in range(1, 10):
            if nums.count(i) % 2 == 1:
                is_palindrom += 1
                if is_palindrom > 1:
                    return False

        return True


# root, expected = [2, 3, 1, 3, 1, None, 1], 2
# result = Solution().pseudoPalindromicPaths(root)

# assert result == expected
        

result = Solution().is_palindrome([2, 1, 1])
assert result is True
