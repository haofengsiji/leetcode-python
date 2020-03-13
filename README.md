# leetcode-python

[TOC]

## Question & Code

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
| 31   | [下一个排列](https://leetcode-cn.com/problems/next-permutation/) | 1.[逻辑思路](https://leetcode-cn.com/problems/next-permutation/solution/) |
| 32   | [最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/) | 1.用栈匹配括号，存下括号索引，对索引进行排序，计算最长连续的索引<br />2.暴力法，遍历所有偶数子字符串，判断是否是有效括号，超时。<br />3.**[动态规划](https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zhan-wei-shi-yao-tou-jie-dian-she-wei-1-by-haofeng/)**，巧妙在转移方程的设置<br />  1."dp[i-2]+()"<br />  2."dp[i-1-dp[i-1]-1]+(+dp[i-1]+)"<br />4.[**栈**]()，巧妙在初始栈顶设为-1，为了当前有效括号和之前有效括号连接上。最快。 |
| 33   | [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | 1.[**二分**](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/jie-zhu-wu-xuan-zhuan-bu-fen-zuo-er-fen-jian-hua-p/)，题目限定，借助二分后，无旋转的部分做判断，简单易理解，当长度为2时就跳出循环，不需要mid+1技巧。 |
| 34   | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 1.[二分](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/bi-jiao-zhi-de-si-lu-by-haofengsiji/)，找到就break，然后在找到位置处向前向后搜索。特殊情况特殊处理。<br />1.[二分](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/)，二分找左边界，二分找右边界，mid 是否+1 -1 很难。 |
| 35   | [搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/) | 1.遍历<br />2.[二分查找](https://leetcode-cn.com/problems/search-insert-position/solution/1biao-zhun-er-fen-2bian-li-by-haofengsiji/) |
| 36   | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/) | 1.[哈希表](https://leetcode-cn.com/problems/valid-sudoku/solution/ha-xi-biao-cha-zhao-python-by-haofengsiji/)，构建3个表，行字典，列字典，方形字典，1-9不能存在重复，用in来判断字典里的列表是否重复，字典(列表)<br />2.哈希表，列表(字典)，判断对应key(1-9)的value(计数)是否大于1。 |
| 38   | [外观数列](https://leetcode-cn.com/problems/count-and-say/)  | 1.直推，借助指2针记录重复和当前<br />2.                      |
| 41   | [缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/) | 1. 官解，保证有1；保证都在1~n内，不是的标1；标记索引的值为负号，代表出现了(索引+1)的正数; 如果全为负数，返回n+1; |
| 42   | [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) | [详细通俗的思路分析，多解法](https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/)<br />1. 按行<br />2.按列，找做左边最高，右边最高，计算当前列可盛水<br />3.动态规划辅助，按列优化，利用空间换时间，先求出左边最高状态和右边最高状态，然后按列求每列可盛水，<br />4.双指针，动态规划的优化，利用每次只用到两个状态，左右开弓<br />5.栈，辅助计算盛水量，如何计算盛水量是难点。 |
| 44   | [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/) | 1.**动态规划**，dp[i]/[j]表示s前i个字符与p前j个字符是否匹配，特殊情况作为初始化状态<br />2. |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | 1.**动态规划**，dp[i]为以nums[i]为结尾的最大和<br />2.       |
| 66   | [加一](https://leetcode-cn.com/problems/plus-one/)           | 1.列表转数字，数字转列表<br />2.                             |
| 84   | [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) | 1.[栈](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/)，用栈来记录转折点，辅助计算最大面积。<br />2. |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 1.[**递归**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/)，中序，左根右<br />2.[**迭代**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/)，借助栈存储之前的节点。 |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | 1.**贪心算法**，转化为今天昨天最大收益<br />2.               |
| 153  | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) | 1.[二分法](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487284&idx=1&sn=9fcdbc39c7961d84fb02ee0807eb620e&chksm=fa0e60b5cd79e9a3101ba10a3f33d4b57fddcdedb6c96899373ad7d66c4583a27ebf7f0855c1&mpshare=1&scene=1&srcid=&sharer_sharetime=1580558866014&sharer_shareid=054d4f86839c6c91a77661fcb8d1a367&key=844c91e610caa57a7099df1d0a6e67a70c481db70ca9be833037d4f95abf1f213e98b5ad236761da6257264adafa12bb1d6dc5043d2bdd4e06d42e3b8d31b2529a6071ac406f9c57b33002902b52817f&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=A2X8BUya8SyYoY%2B%2FkgePiQM%3D&pass_ticket=w%2Bk3LZgLKPLeI80LEJA0Akai7vd4e9r3vCajc2r7UQcDvfogxFo3qv9Fh9Wt6hIs)<br />2.遍历<br />3.min，笔试用 |
| 206  | [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) | 1.[递归](https://leetcode-cn.com/problems/reverse-linked-list/solution/python-di-gui-by-haofengsiji/)，归：特殊情况（到结尾），递，假设前k-1个已经翻转，处理当前第k个节点的操作。尾节点也可以在递的过程中得到<br />2.[双指针](https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/)，巧妙的地方在于初始化，prev=None，curr=head. 所有情况都被普适化了 |
| 237  | [ 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/) | 1.[覆盖](https://mp.weixin.qq.com/s/2XdUeDNblryFpXpTUgsaMQ)下一个值后，跳过下一个节点 |
| 415  | [字符串相加](https://leetcode-cn.com/problems/add-strings/)  | 1.[ASCII码转换](https://leetcode-cn.com/problems/add-strings/solution/python-wu-int-by-haofengsiji/)，不能用int() |
| 646  | [最长数对链](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/) | 1.先排序，后链接                                             |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/)  | 1.[归并排序，**分治算法**，子问题构建新的列表来存储结果](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487045&idx=3&sn=e9f67f1fd33649c60478638c1d6cc2d9&key=86fce317de144aa641d25984adf4d5110a34d6995235ffcd431ddcfaf6b4aeb9037f4e236e4800d46e2c4f7a2c7cc05106593c207c59bf62ae295620cd7c3f3635d80d5092a9deb76305b5e1c7c7d728&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=A6HD67v3cF6uVv%2FgPHwimb0%3D&pass_ticket=nFXyKfVYsTU8JaGrP7IGX7STLom7%2F0YSXb6zJufgedmrCxEsPkmUcfANYDBwOUO8)<br />2.[**冒泡排序**，超时](https://www.youtube.com/watch?v=nmhjrI-aW5o)<br />3.[**快排**，找到中间数（pivot的左边都小于等于pivot的右边和pivot），左右分治](https://www.youtube.com/watch?v=COk73cpQbFQ)<br /> |
| 1103 | [分糖果 II](https://leetcode-cn.com/problems/distribute-candies-to-people/) | 1.遍历，按规则一个一个发<br />2.[数学](https://leetcode-cn.com/problems/distribute-candies-to-people/solution/guan-jie-shu-xue-ji-suan-guo-cheng-by-haofengsiji/)，等差数列 |

## 动态规划

| #    | Title                                                        | Remark                                                       |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 5    | [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/) | method_2                                                     |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | method_3                                                     |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | method_2                                                     |
| 44   | [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/) | method_1                                                     |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | method_1                                                     |
| 62   | [不同路径](https://leetcode-cn.com/problems/unique-paths/)   | 1.[数学](https://leetcode-cn.com/problems/unique-paths/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-20/)，总共要走m+n-2步，其中向右m-1，向左n-1，所以有$C_{m+n-2}^{m-1}$种可能<br />2.[动态规划](https://leetcode-cn.com/problems/unique-paths/solution/62-bu-tong-lu-jing-by-alexer-660/)，写出从小矩阵到大矩阵，有规律，左加上。<br />3.[动态规划](https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-kong-jian-fu-za-du-you-hua-on-pyt/)，优化，利用线程图写出，空间优化为$O(n)$ |
| 63   | [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) | 1.动态规划，障碍当前为0可能路径，注意边界，其他不变<br />2.[动态规划](https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode/)，优化，利用障碍数组作为动态规划数组 |
| 64   | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) | 1.动态规划，类似63，也可以利用网格矩阵作为动态对话矩阵       |
| 70   | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)  | 1.动态规划，当前阶梯，可来自于之前第一个阶梯或者前第二个阶梯<br />2.动态规划，优化，每次变化只联系到两个数<br />3.[递归](https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/)，每次尝试走一步和两步，穷举所有情况，若成功刚好到达指定阶梯，返回1. |
| 85   | [最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/) | 1.[动态规划](https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/)，O(m^2n), dp[i]/[j]表示此行以j为结尾最长连续矩阵，最大连续矩阵需要另算。遍历m*n, 求出以ij为结尾最大面积需要m。dp存的是柱形图。<br />2.[动态规划](https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/)，优化，可以分解为生成柱形图，然后求出柱形图的最大面积(leetcode84)。这里算最大面积，不是嵌套，所以O(mn)。 |
| 174  | [地下城游戏](https://leetcode-cn.com/problems/dungeon-game/) | [动态规划](https://leetcode-cn.com/problems/dungeon-game/solution/dong-tai-gui-hua-by-powcai-8/)，从左下到右上，后方的加血累计不会影响前方扣血 |



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



## 递归/回溯

| #    | 题目                                                         | 备注     |
| ---- | ------------------------------------------------------------ | -------- |
| 17   | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | method_1 |
| 21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | method_2 |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | method_1 |



## 深度优先搜索

| #    | 题目                                                         | 备注                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/) | method_1                                                     |
| 39   | [组合总和](https://leetcode-cn.com/problems/combination-sum/) | 1.[DFS](https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/)，减法，候选值可重复使用，排序，往下递归，残差等于0返回，小于0剪枝<br />2. |
| 40   | [组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/) | 1.[DFS](https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/), 减法，候选值只能用一次，排序，往下递归，递归不包含用过的候选人，残差等于0返回，小于0大剪枝，如果cand[i] == cand[i-1] 小剪枝（避免重复）<br />2. |
| 98   | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/) | 1.递归，当节点为空，返回True; 当val 不满足上界下界，返回False；向右向左递归，若得到False,则返回False;<br />2. |
| 99   | [恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/) | 1.中序遍历，第一个交换节点是：前节点比后节点大中的前节点。第二个交换节点是： 前街店比后节点大中的后节点。 |
| 100  | [相同的树](https://leetcode-cn.com/problems/same-tree/)      | 1. [二叉树框架](https://leetcode-cn.com/problems/same-tree/solution/xie-shu-suan-fa-de-tao-lu-kuang-jia-by-wei-lai-bu-/)，root 的操作；剩下交给框架 |



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



## 高频

| #    | 题目                                                         | 备注                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 5    | [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) | 2.动态规划基础 3.中心扩展优化空间                            |
| 74   | [编辑距离](https://leetcode-cn.com/problems/edit-distance/)  | 1.[动态规划](https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode/) |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 1.递归基础 2.迭代                                            |
| 1143 | [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) | 1.[动态规划](https://leetcode-cn.com/problems/longest-common-subsequence/solution/chao-xiang-xi-dong-tai-gui-hua-jie-fa-by-shi-wei-h/) |

