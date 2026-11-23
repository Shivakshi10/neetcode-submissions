class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = ""

        minLen = 300

        for i in strs:
            minLen = min(len(i), minLen)

        for i in range(minLen):
            localStr = strs[0][i]
            for j in strs:
                if j[i] != localStr:
                    return strr
            strr = strr + localStr
        return strr