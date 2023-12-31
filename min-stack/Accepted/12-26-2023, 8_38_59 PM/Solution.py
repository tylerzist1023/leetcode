// https://leetcode.com/problems/min-stack

class MinStack(object):

    def __init__(self):
        self.stack = [] # contains tuples of (val, min)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((val,val))
        else:
            if val < self.getMin():
                self.stack.append((val,val))
            else:
                self.stack.append((val,self.getMin()))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()