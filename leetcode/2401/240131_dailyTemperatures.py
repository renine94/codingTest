from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        
        for cindex,ctemp  in enumerate(temperatures):
            # cause it is monotonically decreasing
            while stack and stack[-1][0] < ctemp:
                t,i = stack.pop()
                result[i] = cindex - i
            stack.append((ctemp, cindex))
        return result
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     result = [0] * len(temperatures)
        
    #     for i in range(len(temperatures)):
    #         current_temp = temperatures[i]
    #         temp = 1
    #         for j in range(i + 1, len(temperatures)):
    #             next_temp = temperatures[j]
    #             if current_temp < next_temp:
    #                 result[i] = temp
    #                 break
    #             else:
    #                 temp += 1
        
    #     return result
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     result = [0] * (len(temperatures) + 1)

    #     temp_dict = {i: temp for i, temp in enumerate(temperatures, 1)}

    #     for k, v in temp_dict.items():            
    #         for i in range(k+1, len(temperatures)+1):
    #             if v < temp_dict[i]:
    #                 result[k] = i - k
    #                 break
        
    #     return result[1:]



temperatures, expected = [73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]
# temperatures, expected = [30,40,50,60], [1, 1, 1, 0]
result = Solution().dailyTemperatures(temperatures)

assert result == expected

