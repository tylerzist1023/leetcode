// https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        out = []
        
        for s in strs:
            found = False
            for l in out:
                if len(l[0]) == len(s) and self.isAnagram(l[0], s):
                    l.append(s)
                    found = True
            if not found:
                out.append([s])

                
        return out

                

    def isAnagram(self, str1, str2):
        letters = {}
        
        for c in str1:
            if not letters.has_key(c):
                letters[c] = 1
            else:
                letters[c]+=1
        for c in str2:
            if not letters.has_key(c):
                return False
            else:
                letters[c]-=1

        for k in letters:
            if letters[k] != 0:
                return False
        return True