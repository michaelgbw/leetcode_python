#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :硬币兑换问题.py
@说明        :
@时间        :2020/05/13 23:34:19
@作者        :gbw
@版本        :1.0
'''

# 动态规划思想  dp方程式如下
# dp[0] = 0
# dp[i] = min{dp[i - coins[j]] + 1}, 且 其中 i >= coins[j], 0 <= j < coins.length
# 回溯法，输出可找的硬币方案
# path[i] 表示经过本次兑换后所剩下的面值，即 i - path[i] 可得到本次兑换的硬币值。
class Solution():
    def changeCoins(self, coins, n):
        if n < 0: return None
        dp, path = [0] * (n + 1), [0] * (n + 1)  # 初始化
        for i in range(1, n + 1):
            minNum = i  # 初始化当前硬币最优值
            for c in coins:  # 扫描一遍硬币列表，选择一个最优值
                if i >= c and minNum > dp[i - c] + 1:
                    minNum = dp[i - c] + 1
                    path[i] = i - c
            dp[i] = minNum  # 更新当前硬币最优值
    
        print(path)
        return dp[-1]
        
        print('可找的硬币', end=': ')
        while path[n] != 0:
            print(n - path[n], end=' ')
            n = path[n]
        

obj = Solution()
res = obj.changeCoins([1,3,5], 11)
print(res)
