from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        
        for idx, row in enumerate(bank):
            current_beam_cnt = row.count("1")
            for nrow in bank[idx+1:]:
                next_beam_cnt = nrow.count("1")
                if next_beam_cnt == 0:
                    continue
                else:
                    result += current_beam_cnt * next_beam_cnt
                    break
        
        return result




bank, expected = ["011001","000000","010100","001000"], 8
result = Solution().numberOfBeams(bank)
assert result == expected