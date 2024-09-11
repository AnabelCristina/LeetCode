class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
        vowels_index = []
        characteres = []

        for letter in s:
            characteres.append(letter)

        for index, letter in enumerate(characteres):
            if letter in vowels:
                vowels_index.append(index)

        for x in range(math.floor(len(vowels_index)/2)):
            last = len(vowels_index) -1 -x
            temp = characteres[vowels_index[x]]
            characteres[vowels_index[x]] = characteres[vowels_index[last]]
            characteres[vowels_index[last]] = temp

        return "".join([str(i) for i in characteres])
