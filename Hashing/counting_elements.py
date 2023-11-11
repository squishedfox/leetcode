class Solution:
    def counting_elements(self, arr: list[int]) -> int:
        """
        Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

        Example 1:

            Input: arr = [1,2,3]
            Output: 2
            Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

        Example 2:

            Input: arr = [1,1,3,3,5,5,7,7]
            Output: 0
            Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.

        Constraints:

            1 <= arr.length <= 1000
            0 <= arr[i] <= 1000
        """
        num_set = set(arr)
        count = 0

        for num in arr:
            if num + 1 in num_set:
                count += 1

        return count
    
def test_total_count_should_be_2():
    count = Solution().counting_elements([1,2,3])
    assert count == 2, f"Count was {count} but expectd '2'"

def test_total_count_should_be_0():
    count = Solution().counting_elements([1,1,3,3,5,5,7,7])
    assert count == 0, f"Count was {count} but expected '0'"

if __name__ == "__main__":
    test_total_count_should_be_0()
    test_total_count_should_be_2()