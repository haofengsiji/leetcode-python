# leetcode-python

[TOC]

## Question Code

| #    | Title                                                        | Remark                                                       |
| ---- | ------------------------------------------------------------ | :----------------------------------------------------------- |
| 1    | [Two Sum](https://leetcode.com/problems/two-sum/)            | 1.try one by one <br />T: $O(n^2)$ S:$O(1)$<br />2.[find `target - num` (hash_table)](https://leetcode-cn.com/problems/two-sum/solution/dong-hua-tu-jie-suan-fa-liang-shu-zhi-he-fu-shi-pi/)<br /> key: nums -> value: index<br />T: $O(n)$ S: $O(n)$ |
| 2    | [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/) | 1.link2num;num2link<br />T: $O(n)$ S: $O(n)$<br />2.[Link version](https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode/)<br />T: $O(n)$ S: $O(n)$ |
| 3    | [Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | 1.Using set to judge repeating string<br />2.[Sliding Window](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/)<br />T:$O(n)$ S:$O(k)$ |
| 4    | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 1.Brute force(sort firstly,then median)<br />2.[Binary Search in nums1](https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-array.md)<br />T:$O(log(min(m,n)))$ S:$O(1)$ |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | 1.Brute force(loop all the possible str)<br />T:$O(n^3)$  S:$O(1)$<br />2.[Dynamic Programing](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)<br />T：$O(n^2)$ S:$O(n^2)$<br />3. [extend from center to side](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)<br />T：$O(n^2)$ S:$O(1)$ |
| 6    | [ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/) | 1. [Find index math relation](https://leetcode-cn.com/problems/zigzag-conversion/solution/zhao-gui-lu-by-haofengsiji/)<br />T: $O(n)$ S: $O(n)$<br />2. [Use flag to locate index](https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/)<br />T: $O(n)$ S: $O(n)$ |
| 7    | [Reverse Integer](https://leetcode-cn.com/problems/reverse-integer/) | 1. do flips with the help of string<br />2. [**pop** & **push**](https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode/)<br />T: $O(log(x))$ S: $O(1)$ |
| 8    | [String to Integer (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/) | 1.if else<br />T：$O(n)$ S:$O(1)$<br />2.[regular expression](https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/) |
| 9    | [Palindrome Number](https://leetcode-cn.com/problems/palindrome-number/) | 1. [do flips with the help of string](https://leetcode-cn.com/problems/palindrome-number/solution/jie-zhu-strzuo-inverse-by-haofengsiji/)<br />2.[pop](https://leetcode-cn.com/problems/palindrome-number/solution/jie-zhu-strzuo-inverse-by-haofengsiji/)<br />T: $O(log(x))$ S: $O(1)$ |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | 1.re module<br />2.[Backtracking Algorithm](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/)<br />3.[DP](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/)<br />method_2 logic<br />T: $O(mn)$ S: $O(mn)$ |
| 11   | [Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/) | 2. [move the short side](https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/)<br />T：$O(n)$ S:$O(1)$ |
| 12   | [整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/) | 1.按序整除                                                   |
| 13   | [Roman to Integer](https://leetcode-cn.com/problems/roman-to-integer/) | 1. Direct method<br />T：$O(n)$ S:$O(1)$<br />2. [Math trick](https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/)<br />T：$O(n)$ S:$O(1)$ |
| 14   | [Longest Common Prefix](https://leetcode-cn.com/problems/longest-common-prefix/) | 1. <br />2. with help of **set()**<br />3.horizontal scan    |
| 15   | [ 三数之和](https://leetcode-cn.com/problems/3sum/)          | 1.先**排序**帮助判断重复，然后三数之和转为两数之和，两数之和用**hash表查找**，用in判断是否重复<br />2.[先**排序**，固定一个数，然后用**双指针**滑动，重复则跳过](https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/)。 |
| 16   | [最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/) | 1.**排序**+**双指针**                                        |
| 17   | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | 1.[**递归**，abc ->comb(a,comb(b,comb(c,'')))](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/1di-gui-by-haofengsiji/)<br />2.[直推，从前往后，与递归正好相反](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode/) |
| 18   | [四数之和](https://leetcode-cn.com/problems/4sum/)           | 1.**排序**+**双指针**：四数->三数->两数                      |
| 19   | [删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) | 1.**双指针**                                                 |
| 20   | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) | 1.**栈**，左括号，存。右括号，匹配弹出，匹配失败，无效。最后栈为空，则有效。 |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | 1[.构建一个新的列表dummy来存储结果](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487274&idx=3&sn=54d4233b4a6b71992022b38344ed3a0b&chksm=fa0e60abcd79e9bd27c9afce932536fa6f8ef80fde21ab96ebfb59cd3e12894993358ff2647e&scene=126&sessionid=1579499303&key=e24440588457eca66f8057e6b53c40bf9fa6199c5b6ee9bd54d8e4b9ee03faeaee8aa99fbe0a657863a63729772ada929f5501d6f63634d72f55d4730aab0d903572797087bd8290f50192c06179657c&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=AzSO59n6IRjiQBQO%2BTwM77A%3D&pass_ticket=yrjKRiSfNhp8nU3OrHEafWbWOztb5WdZ2KLx5QcB%2BX1KrwXlvHCLWW5%2F%2F%2BYdXarw)<br />2.**[递归](https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/)**，每次弹出一个最小链表，剩下的在扔进函数里，直至一个链表为空，返回非空的链表。<br />3.[迭代，链接，断开。](https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/) |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | 1.[**深度优先搜索**，**递归树**，剪枝](https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/)<br />2.[**动态规划**](https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/)，dp[i] 表示i = n的结果，dp[i] 可由dp[i-1]转移。 |
| 23   | [合并K个排序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | 1.[**分治算法**，巧妙在按序两两分治，而不是左右分治](https://leetcode-cn.com/problems/merge-k-sorted-lists/)<br />2.[暴力法](https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode/)，先存为列表，排序，构建新的链表<br />3.[优先队列](https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode/)，每次将K链表的头放进优先队列，，自动排序后，取出构建新链表。 |
| 24   | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | 1.**指针**，1迭代指针，2位置指针，3前置指针：两种情况：1：头指针交换 2：非头指针交换<br />2.迭代，[**指针**](https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-19/)，额外头节点，普适化，只有非头指针交换，2位置指针，1前置指针<br />3.[**递归**](https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-19/)，只有头指针交换 |
| 25   | [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) | 1.[迭代](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/die-dai-by-haofengsiji/)，额外头节点，普适化，构建k个交换指针加上一个前驱节点<br />2.[递归](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/submissions/)，先处理前k个，后面的递。 |
| 26   | [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) | 1.单**指针**，加pop<br />2.[**双指针**](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/)，运用原数组的空间，很巧妙 |
| 27   | [移除元素](https://leetcode-cn.com/problems/remove-element/) | 1.双指针，将等于val的放后面                                  |
| 28   | [实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/) | 1.没啥可说的<br />2.笔试用find                               |
| 29   | [两数相除](https://leetcode-cn.com/problems/divide-two-integers/) | 1.[位操作](https://leetcode-cn.com/problems/divide-two-integers/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-4/)，除法转为减法（a/b，a中有多少个b），正数转为负数（取反加一），负数累加，避免溢出。 |
| 30   | [串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/) | 1.借用哈希表<br />2.[滑动窗口](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-powcai/)，每次划出，或划入一个单词，记录Counter,方便优化。 |
| 44   | [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/) | 1.**动态规划**，dp[i]/[j]表示s前i个字符与p前j个字符是否匹配，特殊情况作为初始化状态<br />2. |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | 1.**动态规划**，dp[i]为以nums[i]为结尾的最大和<br />2.       |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 1.**递归**，中序，左根右<br />2.                             |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | 1.**贪心算法**，转化为今天昨天最大收益<br />2.               |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/)  | 1.[归并排序，**分治算法**，子问题构建新的列表来存储结果](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487045&idx=3&sn=e9f67f1fd33649c60478638c1d6cc2d9&key=86fce317de144aa641d25984adf4d5110a34d6995235ffcd431ddcfaf6b4aeb9037f4e236e4800d46e2c4f7a2c7cc05106593c207c59bf62ae295620cd7c3f3635d80d5092a9deb76305b5e1c7c7d728&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=A6HD67v3cF6uVv%2FgPHwimb0%3D&pass_ticket=nFXyKfVYsTU8JaGrP7IGX7STLom7%2F0YSXb6zJufgedmrCxEsPkmUcfANYDBwOUO8)<br />2.[**冒泡排序**，超时](https://www.youtube.com/watch?v=nmhjrI-aW5o)<br />3.[**快排**，找到中间数（pivot的左边都小于等于pivot的右边和pivot），左右分治](https://www.youtube.com/watch?v=COk73cpQbFQ)<br /> |

## 动态规划

| #    | Title                                                        | Remark   |
| ---- | ------------------------------------------------------------ | -------- |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | method_2 |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | method_3 |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | method_2 |
| 44   | [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/) | method_1 |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | method_1 |



## 数据结构

| #    | 题目                                                         | 备注                      |
| ---- | ------------------------------------------------------------ | ------------------------- |
| 2    | [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/) | 链表                      |
| 19   | [删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) | 链表                      |
| 20   | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) | 栈                        |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | 链表                      |
| 23   | [合并K个排序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | 链表                      |
| 24   | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | 链表                      |
| 30   | [串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/) | 哈希表                    |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 二叉树，栈 ，中序：左根右 |
|      |                                                              |                           |



## 分治算法

| #    | 题目                                                         | 备注                                             |
| ---- | ------------------------------------------------------------ | ------------------------------------------------ |
| 23   | [合并K个排序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | method_1:两两分治，子问题是合并2个排序链表       |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/)  | 1.归并排序，分治后，子问题用新列表缓存排序的结果 |
|      |                                                              |                                                  |
|      |                                                              |                                                  |



## 贪心算法

| #    | 题目                                                         | 备注    |
| ---- | ------------------------------------------------------------ | ------- |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | method1 |
|      |                                                              |         |
|      |                                                              |         |



## [十大经典排序](https://github.com/hustcc/JS-Sorting-Algorithm)

| #    | 题目                                                        | 备注                |
| ---- | ----------------------------------------------------------- | ------------------- |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/) | method_1:归并排序   |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/) | method_2:冒泡：超时 |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/) | method_3:快排       |



## 递归

| #    | 题目                                                         | 备注     |
| ---- | ------------------------------------------------------------ | -------- |
| 17   | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | method_1 |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | method_2 |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | method_1 |



## 深度优先搜索

| #    | 题目                                                         | 备注     |
| ---- | ------------------------------------------------------------ | -------- |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | method_1 |
|      |                                                              |          |
|      |                                                              |          |



## Floyd-Warshall算法

| #    | 题目                                                         | 备注                     |
| ---- | ------------------------------------------------------------ | ------------------------ |
| 5321 | [阈值距离内邻居最少的城市](https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | leetcode-week173（未看） |
|      |                                                              |                          |
|      |                                                              |                          |



## leetcode周赛

| #    | 题目                                                         | 备注                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 5319 | [删除回文子序列](https://leetcode-cn.com/problems/remove-palindromic-subsequences/) | [leetcode-week173](https://haofengsiji.github.io/2020/01/26/leetcode-week173/) |
| 5320 | [餐厅过滤器](https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/) | [leetcode-week173](https://haofengsiji.github.io/2020/01/26/leetcode-week173/) |
|      |                                                              |                                                              |

