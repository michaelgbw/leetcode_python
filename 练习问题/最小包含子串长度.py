#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 求str1 里面最小包含 str2的长度
# eg:str1:"abcde" str2:"ac"  "abc"是最短的  返回3
import sys

class Solution:
    def convert(self, str1, str2):
        strMap = {}
        if len(str2) > len(str1):
            return 0
        strMap[str2[0]] = 1
        for one in str2[1:]:
            if one in strMap:
                strMap[one] += 1
            else:
                strMap[one] = 1
        left,right = 0,0
        matchmin = sys.maxint
        match = len(str2)
        
        while right != len(str1):
            print(strMap)
            try:
                strMap[str1[right]] -= 1
            except :
                strMap[str1[right]] = -1
            if strMap[str1[right]] >=0:
                match -= 1 
            
            if match ==0:
                
                while strMap[str1[left]] < 0:
                    strMap[str1[left]] += 1
                    left+= 1
                matchmin = min(matchmin,right-left+1)
                match +=1
                strMap[str1[left]] += 1
                left+= 1

            right += 1
        
        return 0 if matchmin == sys.maxint else matchmin

ob = Solution()
res = ob.convert("adabbca","acb")
print(res)



    
