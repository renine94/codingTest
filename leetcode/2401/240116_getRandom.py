# https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/4572981/c-java-python-easiest-solution-with-explanation/

import random

class RandomizedSet:

    def __init__(self):
        self.items = set()

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if self.items:
            return random.choice(list(self.items))
        raise ValueError
        


# Your RandomizedSet object will be instantiated and called as such:
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]

obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()

assert [param_1, param_2, param_3, param_4, param_5, param_6, param_7] == [True, False, True, 2, True, False, 2]