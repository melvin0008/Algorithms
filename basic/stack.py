class MinStack:
    def __init__(self):
        self.minStack=[]
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
        if len(self.minStack)>0:
            if item < self.minStack[-1]:
                self.minStack.append(item)
        else:
            self.minStack.append(item)
    
    def pop(self):
        if len(self.stack)>0:
            item= self.stack.pop()
            if len(self.minStack)>0:
                if item == self.minStack[-1]:
                    self.minStack.pop() 
            return item
            
    def getMin(self):
        if len(self.minStack)==0:
            return None
        return self.minStack[-1]

s=MinStack()
s.push(5)
s.push(6)
s.push(2)
print s.pop()
print s.getMin()
