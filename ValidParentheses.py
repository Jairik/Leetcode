class Solution:
    def isValid(self, s: str) -> bool:
        '''
        You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
        The input string s is valid if and only if:
            - Every open bracket is closed by the same type of close bracket.
            - Open brackets are closed in the correct order.
            - Every close bracket has a corresponding open bracket of the same type.
        '''

        # Creating the Stack
        stack = []

        #Checking each paranthesis
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(i)
            elif s[i] in  [']', '}', ')']:
                stack.pop()

        return not stack #If stack is empty, then paranthesis are valid 

