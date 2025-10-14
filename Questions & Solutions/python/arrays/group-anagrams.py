# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Thought process:
        # 1) Two words are anagrams if they contain the same characters in any order.
        # 2) The simplest way to identify anagrams is by sorting the characters of each word — 
        #    all anagrams will share the same sorted version (e.g., "eat" and "tea" both become "aet").
        # 3) Use a hashmap (defaultdict(list)) to group words by their sorted version as the key.
        #    - Key: tuple(sorted(s)) — we use a tuple because lists can't be dictionary keys.
        #    - Value: list of words (strings) that match that key.
        # 4) After looping through all words, each key in the dictionary will hold one group of anagrams.
        # 5) Finally, collect all grouped values into the result list and return it.
        # 6) Time complexity: O(N * K log K)
        #       - N = number of strings
        #       - K = average length of each string (because sorting each string costs K log K)
        #    Space complexity: O(N * K) for storing the grouped words.
        anagrams_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagrams_map[sorted_s].append(s)

        for value in anagrams_map.values():
            result.append(value)

        return result