class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        hint : *构造所有罗马字符可能值 1,4,5,9  字母前置表示减法
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list