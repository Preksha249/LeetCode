class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sett = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            longest = max(longest, (r-l)+1)
        return longest



        