class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            anagrams[s_sorted] = anagrams.get(s_sorted, []) + [s]

        return list(anagrams.values())