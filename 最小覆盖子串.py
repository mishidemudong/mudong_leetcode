
class Solution:
    def judge(self, t, tmp):
        i = 0
        while i< len(t) and t[i] in tmp:
            i += 1
        if i == len(t):
            return True
        else:
            return False

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        left, right = 0, 0
        min_s = ''
        while right < len(s):
            min_s += s[right]
            right += 1

            tmp = ''
            while self.judge(t, min_s):
                tmp = min_s[0]
                min_s = min_s[1:]

            min_s = tmp + min_s

        return min_s