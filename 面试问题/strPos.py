#coding=utf-8
# https://blog.csdn.net/v_JULY_v/article/details/7041827
class KMP():
    def __init__(self,p):
        self.next = [0 for _ in range(len(p))]
        self.getNext(p)

    def getNext(self,p):
        pLen = len(p)
        self.next[0] = -1
        k = -1 #后坠
        j = 0 #前坠
        while j < pLen -1:
            if k == -1 or p[j] == p[k]:
                j += 1
                k += 1
                if p[j] != p[k]:
                    self.next[j] = k
                else:
                    self.next[j] = self.next[k]
            else:
                k = self.next[k]
    

    def KMPSearch(self,s, p):
        i,j = 0,0
        sLen = len(s)
        pLen = len(p)
        while i < sLen and j < pLen:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = self.next[j]
        if j == pLen:
            return i - j
        return -1 


s = "BBC_ABCDAB_ABCDABCDABDE"
p = "ABCDABD"
obj = KMP(p)
res = obj.KMPSearch(s, p)
print(res)