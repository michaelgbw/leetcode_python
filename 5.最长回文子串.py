#
# @lc app=leetcode.cn id=5 lang=python3
#
# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1 :
            return s
        if len(s) == 0:
            return ""
        sLen = 2 * len(s) + 1
        sadd = self.addBonous(s)
        maxLen = 1
        start = 0
        for i in range(sLen):
            curLenStep = self.centerSpread(sadd,i)
            if curLenStep > maxLen:
                maxLen = curLenStep
                start = int((i-maxLen) / 2)
        return s[start:start + maxLen]


    def addBonous(self,s):
        newStr = ""
        for one in s :
            newStr += one + "#"
        
        return "#" + newStr
    
    def centerSpread(self,s,center):
        i,j = center-1,center+1
        length = len(s)
        step = 0 
        while (i>=0 and j <length and s[i] == s[j]):
            step += 1
            i -= 1
            j += 1
        return step

# @lc code=end

obj = Solution()
s = "babad"
res = obj.longestPalindrome(s)
print(res)

