class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub_len = len(s) / 2
        while sub_len > 0:
            if len(s) % sub_len == 0:
                if self.is_copies(s, s[0:sub_len]):
                    return True
            sub_len -= 1
        return False
    def is_copies(self, s, sub):
        i = 0
        while i < len(s):
            if s[i:i+len(sub)] != sub:
                return False
            i += len(sub)
        return True