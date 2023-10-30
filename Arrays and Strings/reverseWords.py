def reverseWords(s: str) -> str:
    """
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
    """
    ans = ""
    left_bounds = right_bounds = 0
    for i in range(len(s)):
        char = s[i]
        if char == " ":
            end = left_bounds if left_bounds > 0 else -1
            while right_bounds > end:
                ans += s[right_bounds]
                right_bounds -= 1
            right_bounds = left_bounds = i

        if right_bounds == len(s) - 1:
            ans += " "
            while right_bounds >= left_bounds:
                ans += s[right_bounds]
                right_bounds -= 1
            left_bounds = right_bounds = i

        right_bounds += 1

    if ans[len(ans) - 1] == " ":
        ans = ans[:len(ans) - 1]
    if ans[0] == " ":
        ans = ans[1:]

    return ans

print (reverseWords("Let's take LeetCode contest"))
