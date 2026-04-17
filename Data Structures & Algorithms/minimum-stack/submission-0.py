class MinStack:

    def __init__(self):
        self.stack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            tmp= self.stack[-1]
            del self.stack[-1]
            return tmp
        return None
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        res = self.stack[0]
        for elem in self.stack:
            res = min(res, elem)
        return res
