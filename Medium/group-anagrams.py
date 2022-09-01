class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_res = collections.defaultdict(list)
            
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            dict_res[key].append(strs[i])
            
        return dict_res.values()
