class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thing = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            thing[sorteds].append(s)

        return list(thing.values())

        



        