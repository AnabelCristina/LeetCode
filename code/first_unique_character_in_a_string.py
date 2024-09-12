## brute force
class SolutionOne:
    def firstUniqChar(self, s: str) -> int:
        repeated = []

        for index, string_character in enumerate(s):
            substring = s[index+1:]
            if string_character not in repeated:
                for substring_character in substring:
                    if string_character == substring_character:
                        repeated.append(string_character)
                        break
                if string_character not in repeated:
                    return index

        return -1
    
## hash map
class SolutionTwo:
    def firstUniqChar(self, s: str) -> int:
        countMap = {}

        for character in s:
            if (character in countMap):
                countMap[character] += 1
            else:
                countMap[character] = 1

        for index, character in enumerate(s):
            if countMap[character] == 1:
                return index

        return -1