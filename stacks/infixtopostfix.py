class Solution(object):
    def rank(self,s):
        return {
            "*":3,
            "/":3,
            "+":2,
            "-":2,
            "(":1
        }.get(s,0)
        
    def findk(self,op,op1,op2):
        if op=="*":
            return op1*op2
        elif op=="/":
            return op1/op2
        elif op=="+":
            return op1+op2
        elif op=="-":
            return op1-op2
    
    def infix_to_postfix(self,s):
        #1+2*3-4 123*+4-
        st=[]
        result=[]
        for x in s:
            if x in "0123456789":
                result.append(x)
            elif x =="(":
                st.append(x)
            elif x in ['*','/','+','-']:
                while st and self.rank(x)<=self.rank(st[-1]):
                    result.append(st.pop())
                st.append(x)
            elif x ==")":
                top=st.pop()
                while st and top != "(":
                    result.append(top)
                    top=st.pop()
        while st:
            result.append(st.pop())
        return result
    
    def evaluate_postfix(self,s):
        st=[]
        for x in s:
            if x in "0123456789":
                st.append(int(x))
            elif x in ['*','/','+','-']:
                if len(st)>1:
                    f=st.pop()
                    v=st.pop()
                    node=self.findk(x,v,f)
                    st.append(node)
        return st[0]
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.evaluate_postfix("".join(self.infix_to_postfix(s)))

                    
                    
                    
