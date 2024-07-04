We will solve 75 LeetCode practice. The following table shows name of problems with description.

| Number |Problem title| Description|Example|
|--------|-------------|------------|-------|
| 1. |Two Sum| Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.| Input: nums = [2,7,11,15], target = 9, Output: [0,1],Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].|
|2.| Add Two Numbers| You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.| Input: l1 = [2,4,3], l2 = [5,6,4], Output: [7,0,8], Explanation: 342 + 465 = 807.|
|3.|Longest Substring Without Repeating Characters| Given a string s, find the length of the longest 
substring without repeating characters.| Input: s = "abcabcbb", Output: 3, Explanation: The answer is "abc", with the length of 3.| 
|4. | Median of Two Sorted Arrays| Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).| Input: nums1 = [1,3], nums2 = [2], Output: 2.00000, Explanation: merged array = [1,2,3] and median is 2.|
|5. | Longest Palindromic Substring| Given a string s, return the longest palindromic(A string is palindromic if it reads the same forward and backward.) substring in s.| Input: s = "babad", Output: "bab", Explanation: "aba" is also a valid answer.|
|6. | Zigzag Conversion | The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) | Input: s = "PAYPALISHIRING", numRows = 3, Output: "PAHNAPLSIIGYIR" |
|7. | Reverse Integer | Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.| Input: x = 123, Output: 321|
|8. | Merge Strings Alternately |You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.|Input: word1 = "abc", word2 = "pqr" Output: "apbqcr" |
|9. | Greatest Common Divisor of Strings |For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times). Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.| Input: str1 = "ABCABC", str2 = "ABC" Output: "ABC"|
|10. | Reverse Vowels of a String |Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.| Input: s = "leetcode" Output: "leotcede"|
|11. |Reverse Words in a String |Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space. Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces. | Input: s = "  hello world  " Output: "world hello"|
|12. |Product of Array Except Self |Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.| |
|13. |Increasing Triplet Subsequence |Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.| Input: nums = [1,2,3,4,5] Output: true, Input: nums = [5,4,3,2,1] Output: false|
|14. | Move Zeroes |Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.|Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0] |
|15. | Is Subsequence|Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).|Input: s = "abc", t = "ahbgdc" Output: true |
|16. | Max Number of K-Sum Pairs |You are given an integer array nums and an integer k. In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array. Return the maximum number of operations you can perform on the array. |Input: nums = [1,2,3,4], k = 5 Output: 2 |
|17. |Maximum Average Subarray I |You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.| Input: nums = [1,12,-5,-6,50,3], k = 4 Output: 12.75000|
|18. |Maximum Number of Vowels in a Substring of Given Length | Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k. Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.| Input: s = "abciiidef", k = 3 Output: 3|
|19. |Search Insert Position |Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity| nums = [1, 3, 5, 6] target = 5 Output: 2 |
|20. |Same Tree |Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.| Input: p = [1,2,3], q = [1,2,3] Output: true|
|21. | Single Number |Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.| Input: nums = [2,2,1] Output: 1|
|22. | Subsets |Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.|Input: nums = [1,2,3] Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] |
|23. |Rotate Image|You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.|Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [[7,4,1],[8,5,2],[9,6,3]] |
|24. |Maximum Binary Tree |You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm: Create a root node whose value is the maximum value in nums. Recursively build the left subtree on the subarray prefix to the left of the maximum value. Recursively build the right subtree on the subarray suffix to the right of the maximum value. Return the maximum binary tree built from nums.| |
|25. |Max Consecutive Ones III|Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.|Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 Output: 6 Explanation: [1,1,1,0,0,1,1,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined. |
|26. |Longest Subarray of 1's After Deleting One Element |Given a binary array nums, you should delete one element from it.Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray. | Input: nums = [1,1,0,1] Output: 3 Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's. |
|27. | || |
|28. | || |
|29. | || |
|30. | || |
|31. | || |
|32. | || |
|33. | || |
|34. | || |
|35. | || |
|36. | || |
|37. | || |
|38. | || |
|39. | || |
|40. | || |
|41. | || |
|42. | || |
|43. | || |
|44. | || |
|45. | || |
|46. | || |
|47. | || |
|48. | || |
|49. | || |
|50. | || |
|51. | || |
|52. | || |
|53. | || |
|54. | || |
|55. | || |
|56. | || |
|57. | || |
|58. | || |
|59. | || |
|60. | || |
|61. | || |
|62. | || |
|63. | || |
|64. | || |
|65. | || |
|66. | || |
|67. | || |
|68. | || |
|69. | || |
|70. | || |
|71. | || |
|72. | || |
|73. | || |
|74. | || |
|75. | || |



