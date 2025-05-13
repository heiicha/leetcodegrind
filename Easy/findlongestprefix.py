class Solution(object):
    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=len)
        common = []
        otherwords = strs[1:]
        for i in range(len(strs[0])):
            for word in otherwords:
                if i >= len(word) or strs[0][i] != word[i]:
                    if len(common) > 1:
                        return(''.join(common))
                    elif len(common) == 1:
                        return common[0]
                    else:
                        return ""
            common.append(strs[0][i])
        return(''.join(common))

        """
        :type strs: List[str]
        :rtype: str
        """
        