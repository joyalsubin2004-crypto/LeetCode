class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, lenght = len(s) -1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            lenght += 1
            i-=1
        return lenght

      