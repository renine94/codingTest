# https://leetcode.com/problems/destination-city/description/


paths = [["B","C"],["D","B"],["C","A"]]

def solution(paths):
    path_dicts = dict(paths)

    for start, dest in path_dicts.items():
        while dest in path_dicts:
            start = dest
            dest = path_dicts[start]
        else:
            return dest



result = solution(paths)
print(result)