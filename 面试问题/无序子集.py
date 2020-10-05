

class Solution:
    def sublistIncrement(self,nums):
        res = []
        if len(nums) <= 1:
            res.append(nums)
            return res
        
        def df(path,begin):
            res.append(path[:])
            for i in range(begin, len(nums)):
                if len(path)>0 and path[-1] > nums[i]:
                    continue
                
                path.append(nums[i])
                df(path,i+1)
                path.pop()
        
        df([],0)
        return res



obj = Solution()
nums = [9,6,3,5,2,8,12]
print(obj.sublistIncrement(nums))