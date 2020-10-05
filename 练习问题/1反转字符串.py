#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，
# 如把字符串“abcdef”前 面的 2 个字符'a'和'b'移动到字符串的尾部，使得原字符串变成字符串“cdefab”。
# 请写一个函数完 成此功能，要求对长度为 n 的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。

class Solution:
    def reverseString(self,s, m):
        s = [v for _,v in enumerate(s)]
        n = len(s)
        m %= n
        s = self.reverse(s,0,m-1)
        s = self.reverse(s,m,n-1)
        s = self.reverse(s,0,n-1)
        res = ""
        for i in s:
            res += i
        return res
                

    def reverse(self, s, sfrom, sto):
        while sfrom < sto:
            s[sfrom],s[sto] = s[sto],s[sfrom]
            sfrom+= 1
            sto-= 1
        return s


obj = Solution()
s = "abcdefg"
m = 3
res = obj.reverseString(s,m)
print(res)
    

            