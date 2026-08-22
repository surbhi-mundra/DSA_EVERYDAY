class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        found_alphabet=set()

        for char in sentence:
            found_alphabet.add(char)

            if len(found_alphabet)==26:
                return True

        return False
