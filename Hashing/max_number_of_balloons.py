class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
        You can use each character in text at most once. Return the maximum number of instances that can be formed.

        See: https://leetcode.com/problems/maximum-number-of-balloons
        
        Example 1:

            Input: text = "nlaebolko"
            Output: 1

        Example 2:

            Input: text = "loonbalxballpoon"
            Output: 2

        Example 3:

            Input: text = "leetcode"
            Output: 0

        Constraints:

            1 <= text.length <= 104
            text consists of lower case English letters only.
        """
        count_dict = dict[str, int]({
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        })
        letter_weight = dict[str, int]({
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        })

        for char in text:
            if char in letter_weight.keys():
                count_dict[char] += 1
    
        min_number = None    
        for char, char_seen_count in count_dict.items():
            if min_number is None:
                min_number = char_seen_count
                continue

            min_number = min(min_number, char_seen_count // letter_weight.get(char))

        return min_number