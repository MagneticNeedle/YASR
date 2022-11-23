from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote) : return False
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        all([c2[key] >= count for key, count in c1.items()])