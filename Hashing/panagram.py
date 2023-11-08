class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        A pangram is a sentence where every letter of the English alphabet appears at least once.

        Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

        

        Example 1:

        Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
        Output: true
        Explanation: sentence contains at least one of every letter of the English alphabet.

        Example 2:

        Input: sentence = "leetcode"
        Output: false

        

        Constraints:

            1 <= sentence.length <= 1000
            sentence consists of lowercase English letters.
        """
        if len(sentence) < 26:
            return False # we know for a fact that there are not all 26 American English Characters
        
        character_set = set()
        for char in sentence:
            if char in character_set: # O(1) operation
                continue
            character_set.add(char)

        return len(character_set) == 26
