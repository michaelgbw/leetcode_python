#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file          :207.课程表.py
@explain       :
@time          :2020/12/03 17:35:52
@author        :bangwei gong
@version       :1.0
@usage         :
'''


# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        courseDict = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        for x,y in prerequisites:
            courseDict[x].append(y)
        #开始遍历
        for idx in range(numCourses):
            if not self.DFS(idx,courseDict,visited):
                return False
        
        return True
    def DFS(self, idx, courseDict, visited):
        if visited[idx] == -1:
            return False
        if visited[idx] == 1:
            return True
        #没有出度的点
        if not courseDict[idx]:
            visited[idx] = 1
            return True
        visited[idx] = -1
        for nIdx in courseDict[idx]:
            if not self.DFS(nIdx, courseDict, visited):
                return False
        visited[idx] = 1
        return True
            
# obj = Solution()
# a = obj.canFinish(3,[[1,2], [0,1], [0,2]])
# print(a)
# @lc code=end

