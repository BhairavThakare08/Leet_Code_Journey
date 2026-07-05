class Solution(object):
    def longestCommonPrefix(self, strs):

        first = strs[0]

        for i in range(len(first)):

            for string in strs[1:]:

                if i >= len(string) or string[i] != first[i]:
                    return first[:i]

        return first