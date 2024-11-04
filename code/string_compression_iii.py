class Solution:
    def compressedString(self, word: str) -> str:
        
        comp = ""
        curr = ""
        repeating_times = 0

        for index, letter in enumerate(word):
            if curr == "":
                curr = letter
                repeating_times = 1
            elif curr == letter:
                repeating_times += 1
            else:
                while repeating_times > 9:
                    comp += comp.join(str(9))
                    comp += comp.join(curr)
                    repeating_times -= 9
                comp += comp.join(str(repeating_times))
                comp += comp.join(curr)
                curr = letter
                repeating_times = 1

        while repeating_times > 9:
            comp += comp.join(str(9))
            comp += comp.join(curr)
            repeating_times -= 9
        comp += comp.join(str(repeating_times))
        comp += comp.join(curr)

        return comp
