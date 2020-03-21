class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxx = 0
        for i in range(0,length):
            sub = s[i]
            a = set()
            a.add(sub)
            cnt = 1
            if cnt > maxx:
                maxx = cnt
            for j in s[i+1:]:
                if j not in a:
                    cnt += 1
                    a.add(j)
                    if cnt > maxx:
                        maxx = cnt
                else:
                    break
        return maxx