# https://leetcode.com/problems/implement-queue-using-stacks/?envType=daily-question&envId=2024-01-29
# List 를 이용하여 MyQueue 자료구조 구현하기

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()