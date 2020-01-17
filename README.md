# leetcode-python

[TOC]

## Question Code

| #    | Title                                                        | Solution                                                     | Remark                                                       |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | :----------------------------------------------------------- |
| 1    | [Two Sum](https://leetcode.com/problems/two-sum/)            | [python](https://github.com/haofengsiji/Myleetcode-python/blob/master/Qustion%20Code/1.Two%20Sum.py) | 1.try one by one <br />T: $O(n^2)$ S:$O(1)$<br />2.[find `target - num` (hash_table)](https://leetcode-cn.com/problems/two-sum/solution/dong-hua-tu-jie-suan-fa-liang-shu-zhi-he-fu-shi-pi/)<br /> key: nums -> value: index<br />T: $O(n)$ S: $O(n)$ |
| 2    | [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/2.Add%20Two%20Numbers.py) | 1.link2num;num2link<br />T: $O(n)$ S: $O(n)$<br />2.[Link version](https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode/)<br />T: $O(n)$ S: $O(n)$ |
| 3    | [Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py) | 1.Using set to judge repeating string<br />2.[Sliding Window](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/)<br />T:$O(n)$ S:$O(k)$ |
| 4    | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [python](https://github.com/haofengsiji/Myleetcode-python/blob/master/Qustion%20Code/4.%20Median%20of%20Two%20Sorted%20Arrays.py) | 1.Brute force(sort firstly,then median)<br />2.[Binary Search in nums1](https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-array.md)<br />T:$O(log(min(m,n)))$ S:$O(1)$ |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/5.%20Longest%20Palindromic%20Substring.py) | 1.Brute force(loop all the possible str)<br />T:$O(n^3)$  S:$O(1)$<br />2.[Dynamic Programing](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)<br />T：$O(n^2)$ S:$O(n^2)$<br />3. [extend from center to side](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)<br />T：$O(n^2)$ S:$O(1)$ |
| 6    | [ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/6.%20ZigZag%20Conversion.py) | 1. [Find index math relation](https://leetcode-cn.com/problems/zigzag-conversion/solution/zhao-gui-lu-by-haofengsiji/)<br />T: $O(n)$ S: $O(n)$<br />2. [Use flag to locate index](https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/)<br />T: $O(n)$ S: $O(n)$ |
| 7    | [Reverse Integer](https://leetcode-cn.com/problems/reverse-integer/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/7.%20Reverse%20Integer.py) | 1. do flips with the help of string<br />2. [pop & push](https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode/)<br />T: $O(log(x))$ S: $O(1)$ |
| 8    | [String to Integer (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/8.%20String%20to%20Integer%20(atoi).py) | 1.if else<br />T：$O(n)$ S:$O(1)$<br />2.[regular expression](https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/) |
| 9    | [Palindrome Number](https://leetcode-cn.com/problems/palindrome-number/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/9.%20Palindrome%20Number.py) | 1. [do flips with the help of string](https://leetcode-cn.com/problems/palindrome-number/solution/jie-zhu-strzuo-inverse-by-haofengsiji/)<br />2.[pop](https://leetcode-cn.com/problems/palindrome-number/solution/jie-zhu-strzuo-inverse-by-haofengsiji/)<br />T: $O(log(x))$ S: $O(1)$ |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/10.%20Regular%20Expression%20Matching.py) | 1.re module<br />2.[Backtracking Algorithm](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/)<br />3.[DP](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/)<br />method_2 logic<br />T: $O(mn)$ S: $O(mn)$ |
| 13   | [Roman to Integer](https://leetcode-cn.com/problems/roman-to-integer/) | python                                                       | 1. Direct method<br />T：$O(n)$ S:$O(1)$<br />2. [Math trick](https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/)<br />T：$O(n)$ S:$O(1)$ |

## Dynamic programming

​	

| #    | Title                                                        | Remark   |
| ---- | ------------------------------------------------------------ | -------- |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | method_2 |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | method_3 |
|      |                                                              |          |



