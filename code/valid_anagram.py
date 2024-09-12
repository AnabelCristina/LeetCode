class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        for original_character in s:
            flag = False
            for anagram_character in t:
                if original_character == anagram_character:
                    s=s.replace(original_character,"",1)
                    t=t.replace(anagram_character,"",1)
                    flag = True
                    break
            
            if flag == False:
                return False

        return True
