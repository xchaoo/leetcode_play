class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        hint : 利用栈,左括号来压入，右括号来弹出比较或空栈为F
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] =='[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop()!='(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop()!='[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop()!='{':
                    return False
        if stack:
            return False
        else:
            return True
