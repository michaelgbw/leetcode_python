#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file          :1044.最长重复子串.py
@explain       :
@time          :2020/11/17 21:26:35
@author        :bangwei gong
@version       :1.0
@usage         :
'''


# @lc app=leetcode.cn id=1044 lang=python
# @lc code=start
# 后缀数组解决
class Solution2:
    def longestDupSubstring(self, s):
        if len(s) <= 1:
            return s
        sList = self.GenList(s)
        sListFin = self.HandeQsortlList(sList)
        maxLen = 0
        maxLenIndex = 0
        for i in range(0,len(sListFin)-1):
            icmp = self.comlen(sListFin[i],sListFin[i+1])
            if icmp > maxLen:
                maxLen = icmp
                maxLenIndex = i
            if maxLen == 0:
                return ""
        return sListFin[maxLenIndex][:maxLen]
                
        
    def GenList(self,s):
        res = [];i = 1;a = s
        while len(a) >0:
            res.append(a)
            a = s[i:]
            i+=1
        return res
    
    def HandeQsortlList(self,sList):
        def mysort(a,b):
            i = 0
            while 1:
                if len(a) <= i:
                    return -1
                if len(b) <= i:
                    return 1
                if ord(a[i]) < ord(b[i]):
                    return -1
                if ord(a[i]) > ord(b[i]):
                    return 1
                i += 1
            return 0
        res = sorted(sList,mysort)
        return res
    def comlen(self,a,b):
        maxLen = min(len(a),len(b))
        res = 0
        for i in range(0,maxLen):
            if a[i] != b[i]:
                break
            res +=1 
        return res


class Solution:
    def longestDupSubstring(self, S):
        import functools
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        n = len(S)
        def test(l):
            p = pow(26,l,mod)
            cur = functools.reduce(lambda x,y:(x*26+y)%mod,A[:l])
            seed = {cur}
            for index in range(l,n):
                cur =(cur * 26 + A[index] - A[index-l] * p) % mod
                if cur in seed:
                    return index - l + 1
                seed.add(cur)
            return -1
        low,high = 0,n
        res = 0
        while low < high:
            mid = (low + high + 1) // 2
            pos = test(mid)
            if pos != -1:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res:res+low]


obj = Solution()
s = "fmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglaneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejaneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"
a = obj.longestDupSubstring(s)
print(a)
# @lc code=end

