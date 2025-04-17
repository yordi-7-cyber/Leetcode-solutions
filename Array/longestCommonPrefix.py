class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for strings in strs[1:]:
            while not strings.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix

sol=Solution()
strs=["flower","flow","flight"]
result=sol.longestCommonPrefix(strs)
print(result)
        