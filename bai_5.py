class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        s.sort()
        g.sort()
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j]>=g[i]:
                    c+=1
                    s.remove(s[j])
                    break
                else:
                    continue
        return c
        
        