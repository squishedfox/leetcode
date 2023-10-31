def reverse_only_letters(s: str) -> str:
  """
  Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

  Return s after reversing it.

  Example 1:

    Input: s = "ab-cd"
    Output: "dc-ba"
  
  Example 2:
  
    Input: s = "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
  
  Example 3:
  
    Input: s = "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

  :see: https://leetcode.com/problems/reverse-only-letters/description/
  """
  left_bounds = 0
  right_bounds = len(s) - 1
  ans = [""] * len(s)
  while left_bounds <= right_bounds:
      if not s[right_bounds].isalpha():
          # leave the left character where it is because there is nothing to switch
          ans[right_bounds] = s[right_bounds]
          right_bounds -= 1
          continue
      if not s[left_bounds].isalpha():
          # leave the right character where it is because there is nothing to switch
          ans[left_bounds] = s[left_bounds]
          left_bounds += 1
          continue
          
      ans[left_bounds] = s[right_bounds]
      ans[right_bounds] = s[left_bounds]
      left_bounds += 1
      right_bounds -= 1
  
  return ''.join(ans)

