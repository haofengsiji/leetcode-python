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
| 11   | [Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/11.%20Container%20With%20Most%20Waterost%20Water.py) | 2. [move the short side](https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/)<br />T：$O(n)$ S:$O(1)$ |
| 12   | [整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/) | python                                                       | 1.按序整除                                                   |
| 13   | [Roman to Integer](https://leetcode-cn.com/problems/roman-to-integer/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/13.%20Roman%20to%20Integer.py) | 1. Direct method<br />T：$O(n)$ S:$O(1)$<br />2. [Math trick](https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/)<br />T：$O(n)$ S:$O(1)$ |
| 14   | [Longest Common Prefix](https://leetcode-cn.com/problems/longest-common-prefix/) | [python](https://github.com/haofengsiji/leetcode-python/blob/master/Qustion%20Code/14.%20Longest%20Common%20Prefix.py) | 1. <br />2. with help of set()<br />3.horizontal scan        |
| 15   | [ 三数之和](https://leetcode-cn.com/problems/3sum/)          | python                                                       | 1.先排序帮助判断重复，然后三数之和转为两数之和，两数之和用hash表查找，用in判断是否重复<br />2.先排序，固定一个数，然后用双指针滑动，重复则跳过。 |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | python                                                       | 1[.构建一个新的列表dummy来存储结果](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487274&idx=3&sn=54d4233b4a6b71992022b38344ed3a0b&chksm=fa0e60abcd79e9bd27c9afce932536fa6f8ef80fde21ab96ebfb59cd3e12894993358ff2647e&scene=126&sessionid=1579499303&key=e24440588457eca66f8057e6b53c40bf9fa6199c5b6ee9bd54d8e4b9ee03faeaee8aa99fbe0a657863a63729772ada929f5501d6f63634d72f55d4730aab0d903572797087bd8290f50192c06179657c&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=AzSO59n6IRjiQBQO%2BTwM77A%3D&pass_ticket=yrjKRiSfNhp8nU3OrHEafWbWOztb5WdZ2KLx5QcB%2BX1KrwXlvHCLWW5%2F%2F%2BYdXarw)<br />2.[递归](https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/) |

## 动态规划

​	

| #    | Title                                                        | Remark   |
| ---- | ------------------------------------------------------------ | -------- |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | method_2 |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | method_3 |
|      |                                                              |          |

## 数据结构

| #    | 题目                                                         | 备注 |
| ---- | ------------------------------------------------------------ | ---- |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | 链表 |
|      |                                                              |      |
|      |                                                              |      |



## 分治算法

| #    | 题目                                                        | 备注             |
| ---- | ----------------------------------------------------------- | ---------------- |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/) | 1.归并排序，分治 |
|      |                                                             |                  |
|      |                                                             |                  |



## 贪心算法

## 排序