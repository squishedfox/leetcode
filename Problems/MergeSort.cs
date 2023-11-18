using System;

public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        var left = 0;
        for (var i = 0; i < n; ++i) {
            // because hey are in ascending order we can 
            while (nums1[left] < nums2[i] && left < m + i) {
                left++;
            }

            // first shift all the numbers to the right
            for (var j = m + i; j > left; --j) {
                nums1[j] = nums1[j - 1];
            }

            nums1[left] = nums2[i];
            left++;
        }
    }
}
