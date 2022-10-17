class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pan="abcdefghijklmnopqrstuvwxyz"
        for i in pan:
            if i not in sentence:
                return False
        return True