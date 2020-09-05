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
| 10   | [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/) | 1.正则表达式<br />2.[递归](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/)<br />3.[动态规划](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/) |
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
| 35   | [搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/) | 1.遍历<br />2.[二分法](https://haofengsiji.github.io/2020/06/28/%E7%AE%97%E6%B3%95-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE/)，查找变式 |
| 36   | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/) | 1.[哈希表](https://leetcode-cn.com/problems/valid-sudoku/solution/ha-xi-biao-cha-zhao-python-by-haofengsiji/)，构建3个表，行字典，列字典，方形字典，1-9不能存在重复，用in来判断字典里的列表是否重复，字典(列表)<br />2.哈希表，列表(字典)，判断对应key(1-9)的value(计数)是否大于1。 |
| 37   | [解数独](https://leetcode-cn.com/problems/sudoku-solver/)    | 1.[回溯](https://leetcode-cn.com/problems/sudoku-solver/solution/zi-cong-wo-xue-hui-liao-hui-su-suan-fa-zhong-yu-hu/)，穷举 |
| 38   | [外观数列](https://leetcode-cn.com/problems/count-and-say/)  | 1.直推，借助指2针记录重复和当前<br />2.                      |
| 41   | [缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/) | 1. 官解，保证有1；保证都在1~n内，不是的标1；标记索引的值为负号，代表出现了(索引+1)的正数; 如果全为负数，返回n+1; |
| 42   | [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) | [详细通俗的思路分析，多解法](https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/)<br />1. 按行<br />2.按列，找做左边最高，右边最高，计算当前列可盛水<br />3.动态规划辅助，按列优化，利用空间换时间，先求出左边最高状态和右边最高状态，然后按列求每列可盛水，<br />4.双指针，动态规划的优化，利用每次只用到两个状态，左右开弓<br />5.栈，辅助计算盛水量，如何计算盛水量是难点。 |
| 43   | [字符串相乘](https://leetcode-cn.com/problems/multiply-strings/) | [1](https://leetcode-cn.com/problems/multiply-strings/solution/gao-pin-mian-shi-xi-lie-zi-fu-chuan-cheng-fa-by-la/).竖列乘法模拟，找准对应位就好 |
| 44   | [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/) | 1.**动态规划**，dp[i]/[j]表示s前i个字符与p前j个字符是否匹配，特殊情况作为初始化状态<br />2. |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | 1.**动态规划**，dp[i]为以nums[i]为结尾的最大和<br />2.       |
| 54   | [螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)  | 1.向右-向下-向左-向上，4个边界<br />[2](https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby).每次pop第一行，然后用[\*zip(\*matrix)[::-1]] 旋转矩阵，false and  [operation] 短路操作结束递归 |
| 66   | 难度中等383收藏分享切换为英文关注反馈[加一](https://leetcode-cn.com/problems/plus-one/) | 1.列表转数字，数字转列表<br />2.                             |
| 67   | [二进制求和](https://leetcode-cn.com/problems/add-binary/)   | 1.内置函数，转10进制求和，转2进制输出<br />2.逐位计算，//求进位，%求当前位<br />3.位操作，&求进位和结果，^求无进位和，然后循环计算进位和结果与无进位和结果，直到进位和为零 |
| 84   | [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) | 1.[栈](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/)，用栈来记录转折点，辅助计算最大面积。<br />2. |
| 93   | [复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/) | 1. 递归回溯，若函数中的函数则参数应当是索引，若需要矩阵，则需要创建方法<br />2. 迭代，遍历三个间隔的可能位置 |
| 94   | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 1.[**递归**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/)，中序，左根右<br />2.[**迭代**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/)，借助栈存储之前的节点。 |
| 95   | [不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/) | 1. [递归](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode-solut/)，根节点i，左子树节点候选集[start,i-1],右子树节点候选集[i+1,end]<br />2. [递归+记忆化](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/he-qian-mian-man-er-cha-shu-de-ti-ting-xiang-de-by/)，memo\[start][end] |
| 96   | [不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/) | 1. [动态规划](https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/), $G(n)=\sum_{i=1}^{n} G(i-1) \cdot G(n-i)$<br />2. [递归](https://leetcode-cn.com/problems/unique-binary-search-trees/solution/shou-hua-tu-jie-san-chong-xie-fa-dp-di-gui-ji-yi-h/)，加记忆化<br />3. [卡塔兰数](https://baike.baidu.com/item/catalan/7605685?fr=aladdin)，h(n) = (4n-2)/(n+1)\*h(n-1)  (n>=1)， h(0)=1 |
| 97   | [交错字符串](https://leetcode-cn.com/problems/interleaving-string/) | [官解](https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/)<br />1.动态规划，$f(i, j)=\left[f(i-1, j) \text { and } s_{1}(i-1)=s_{3}(p)\right]$ or $\left[f(i, j-1) \text { and } s_{2}(j-1)=s_{3}(p)\right]$<br />2.根据更新的延迟性，对空间进行优化 |
| 101  | [对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/) | [官解](https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/)，左子树是否等于右子树<br />1.递归<br />2.迭代，队列 |
| 104  | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) | [官解](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/)<br />1. 递归<br />2. BFS |
| 108  | [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/) | 1.[官解](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/)，二叉树搜索树中序遍历是升序序列 |
| 111  | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) | 1.递归，考虑三种情况，1.左右都非空 2.左非空右空 3.右非空左空<br />2. |
| 112  | [路径总和](https://leetcode-cn.com/problems/path-sum/)       | [官解](https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/)<br />1.递归遍历<br />2.广度搜索遍历 |
| 114  | [二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/) | [官解](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/)<br />1. 前序遍历，递归/迭代，然后构建链表<br />2. 前序遍历并同时构建链表，用stack记录右节点信息<br />3. 寻找前驱节点 |
| 120  | [三角形最小路径和](https://leetcode-cn.com/problems/triangle/) | 1. [动态规划](https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/)（官解从上到下），左边界，右边界(特殊情况) 转移公式 + 常规转移公式：dp\[i][j] = min(dp\[i-1][j],dp\[i-1][j-1]) + triangle\[i][j] <br />PS:  [从下到上](https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/)，并且dp数组行列加1可以 将边界情况普适化<br />2. [动态规划](https://leetcode-cn.com/problems/triangle/solution/dong-tai-gui-hua-li-yong-yan-chi-jin-xing-kong-jia/)，利用延迟性，进行空间优化<br />3. DFS + 记忆化 |
| 121  | [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | 1.遍历，比较所有交易<br />2.一次买卖，所以找到历史最低，然后找买入后历史最高 |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | 1.**贪心算法**，转化为今天昨天最大收益<br />2.               |
| 125  | [验证回文串](https://leetcode-cn.com/problems/valid-palindrome/) | [官解](https://leetcode-cn.com/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-by-leetcode-solution/)，字符串处理，string.isalnum() = string.isaplha & string.isdigit |
| 126  | [[单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)](https://leetcode-cn.com/problems/word-ladder-ii/) | [1](https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/). BFS 构建图，得到邻接表，DFS找短路径<br />2. |
| 128  | [最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/) | 1.[哈希表](https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/)，查找 x+1，并根据 x-1 去重 |
| 136  | [只出现一次的数字](https://leetcode-cn.com/problems/single-number/) | 1.哈希表<br />2.XOR，a$\oplus$a$\oplus$b = 0$\oplus$b = b (数学白学了:sweat_smile:) |
| 139  | [单词拆分](https://leetcode-cn.com/problems/word-break/)     | [天使爆破团的解](https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/)<br />1. DFS，递归以位置i开始的字符串能否由字典组成，并记录结果，避免重复递归<br />2. BFS，维护以位置i开始的字符串能否由字典组成的队列，记录是否访问过，避免重复遍历<br />3. DP，dp[i] 前i个字符能否由字典组成，转移条件是i可以拆分成dp[j] == True & s[j:i] in wordDict |
| 146  | [LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)   | [官解](https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/)<br />1.内建OrderedDict，双链表哈希表数据结构<br />2.自己构建 双链表+哈希结构 |
|      |                                                              |                                                              |
| 152  | [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/) | 1.[DP](https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/)<br />$f_{\max }(i)=\max _{i=1}^{n}\left\{f_{\max }(i-1) \times a_{i}, f_{\min }(i-1) \times a_{i}, a_{i}\right\}$<br/>$f_{\min }(i)=\min _{i=1}^{n}\left\{f_{\max }(i-1) \times a_{i}, f_{\min }(i-1) \times a_{i}, a_{i}\right\}$ |
| 153  | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) | 1.[二分法](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487284&idx=1&sn=9fcdbc39c7961d84fb02ee0807eb620e&chksm=fa0e60b5cd79e9a3101ba10a3f33d4b57fddcdedb6c96899373ad7d66c4583a27ebf7f0855c1&mpshare=1&scene=1&srcid=&sharer_sharetime=1580558866014&sharer_shareid=054d4f86839c6c91a77661fcb8d1a367&key=844c91e610caa57a7099df1d0a6e67a70c481db70ca9be833037d4f95abf1f213e98b5ad236761da6257264adafa12bb1d6dc5043d2bdd4e06d42e3b8d31b2529a6071ac406f9c57b33002902b52817f&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=A2X8BUya8SyYoY%2B%2FkgePiQM%3D&pass_ticket=w%2Bk3LZgLKPLeI80LEJA0Akai7vd4e9r3vCajc2r7UQcDvfogxFo3qv9Fh9Wt6hIs)<br />2.遍历<br />3.min，笔试用 |
| 167  | [ 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | 1. [双指针](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/liang-shu-zhi-he-ii-shu-ru-you-xu-shu-zu-by-leet-2/)<br />2. [二分查找](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/)，暴力n^2 -> 二分查找优化nlogn |
| 169  | [多数元素](https://leetcode-cn.com/problems/majority-element/) | [官解](https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/)<br />1.构建字典表，比较数量<br />2.排序，返回nums[n//2]<br />3. |
| 174  | [地下城游戏](https://leetcode-cn.com/problems/dungeon-game/) | 1. [动态规划](https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/)，dp\[i\]\[j\]为\[i,j\]到终点所需的最小初始值，需要从后往前遍历，满足无后效性。从前往后则需要考虑，「从出发点到当前点的路径和」和「从出发点到当前点所需的最小初始值」<br />2. [DFS](https://leetcode-cn.com/problems/dungeon-game/solution/jian-dan-dfskan-yi-yan-jiu-ming-bai-e-by-sweetiee/)，DFS + 记忆化 |
| 206  | [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) | 1.[递归](https://leetcode-cn.com/problems/reverse-linked-list/solution/python-di-gui-by-haofengsiji/)，归：特殊情况（到结尾），递，假设前k-1个已经翻转，处理当前第k个节点的操作。尾节点也可以在递的过程中得到<br />2.[双指针](https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/)，巧妙的地方在于初始化，prev=None，curr=head. 所有情况都被普适化了 |
| 209  | [长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/) | [官解](https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/)<br />1. 暴力，遍历所有子串<br />2. 双指针，滑动窗口<br />3. 暴力优化，前缀和存储换时间，二分查找 prefix[i+1]-s>= prefix[j] |
| 210  | [课程表 II](https://leetcode-cn.com/problems/course-schedule-ii/) | [官解](https://leetcode-cn.com/problems/course-schedule-ii/solution/ke-cheng-biao-ii-by-leetcode-solution/)<br />1. DFS, 根节点入栈<br />2. BFS, 入度为零为前置课程，先修为敬 |
| 237  | [ 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/) | 1.[覆盖](https://mp.weixin.qq.com/s/2XdUeDNblryFpXpTUgsaMQ)下一个值后，跳过下一个节点 |
| 238  | [除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self/) | 1.[前后缀和](https://leetcode-cn.com/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/)<br />2.[双指针](https://leetcode-cn.com/problems/product-of-array-except-self/solution/python-1ge-forxun-huan-gao-ding-by-haofengsiji/) |
| 287  | [寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/) | 官解<br />1.二分法，[1,n]二分，遍历统计小于等于mid的数量是否大于mid,如果是则说明[1,mid]无重复，如果不是[1,mid]有重复<br />2.a*=(*k*−1)*L*+(*L*−*b*)=(*k*−1)*L*+*c, 起点到环步数a = 相遇位置到环入口步数c + k-1次环遍历 |
| 289  | [生命游戏](https://leetcode-cn.com/problems/game-of-life/)   | 1.[遍历](https://leetcode-cn.com/problems/game-of-life/solution/sheng-ming-you-xi-by-leetcode-solution/)细胞，遍历邻居，根据规则更新细胞板，使用额外状态利用原数组空间<br />2.[卷积](https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/) |
| 297  | [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) | 1. [DFS](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/), 递归，左子树序列化，右子树序列化交给小弟<br />2. [BFS](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/), 队列处理，左子树右子树 |
| 300  | [最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) | 1.[动态规划](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)，dp[i]： 以i结尾的最长子序列<br />2.[贪心](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)+二分查找 |
| 312  | [戳气球](https://leetcode-cn.com/problems/burst-balloons/)   | [官解](https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/)<br />1. DFS+记忆，自顶向下，戳气球变成添加气球，这样保证无后效性<br />2. 动态规划，自底向上 |
| 315  | [计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/) | 1.暴力<br />2.[树状数组优化](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/)，维护一个离散的树状数组和对应的前缀和，树状数组[补充材料](https://www.cnblogs.com/xenny/p/9739600.html) |
| 322  | [零钱兑换](https://leetcode-cn.com/problems/coin-change/)    | 1.[DFS(会超时)](https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/)，所以需要乘法优化，贪心找到一个半优解后剪枝<br />2.[动态规划，自顶向下](https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/)，使用备忘录避免重复，dp[amount] = 最少硬币数量<br />3.[动态规划](https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/)，自底向上，使用备忘录避免重复，最自然。 |
| 329  | [矩阵中的最长递增路径](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/) | 1. [DFS](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-by-le-2/)，dfs(row,col)返回当前最大的路径<br />2. |
| 332  | [重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/) | 1. [DFS](https://leetcode-cn.com/problems/reconstruct-itinerary/solution/zhong-xin-an-pai-xing-cheng-by-leetcode-solution/), 根据邻接表构建图，{Node: [nbr1..,nbr2,..]}, dfs 遍历，字符自然排序最小，可以构建最小堆来pop，抓住特性，度为1的一定是最后一个。 |
| 343  | [整数拆分](https://leetcode-cn.com/problems/integer-break/)  | 1. 找规律，尽量取相等的，最显而易见的数学规律<br />[官解](https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/)<br />2. 动态规划，dp[i] = max{1<j<i}(max( j * dp[i - j], j * (i - j))), 单独拎出j, 剩下的分成2个，或者多个<br />3. 数学优化动态规划，只要找 j = 2 或者 j = 3 即可<br />4. 数学， 分成多个3 |
| 350  | [两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/) | [官解](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode-solution/)<br />1.哈希表，查count<br />2.双指针，排序后采用滑动指针<br />3.内置方法，collections.Counter() + & + list(res.elements)  （官解评论） |
| 392  | [判断子序列](https://leetcode-cn.com/problems/is-subsequence/) | [官解](https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/)<br />1. 双指针，缺点每次查询需要遍历一遍t<br />2. 动态规划，预处理t，将查找下一个字符降到O(1). |
| 409  | [最长回文串](https://leetcode-cn.com/problems/longest-palindrome/) | 1.统计偶数，中心+1                                           |
| 410  | [分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/) | 1. [动态规划](https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/), 「将数组分割为 m*m* 段，求……」是动态规划题目常见的问法。<br />2. [二分查找](https://leetcode-cn.com/problems/split-array-largest-sum/solution/wo-geng-xi-huan-de-er-fen-xie-fa-by-haofengsiji/)， 「使……最大值尽可能小」是二分搜索题目常见的问法。 |
| 415  | [字符串相加](https://leetcode-cn.com/problems/add-strings/)  | 1.[ASCII码转换](https://leetcode-cn.com/problems/add-strings/solution/python-wu-int-by-haofengsiji/)，不能用int() |
| 443  | [压缩字符串](https://leetcode-cn.com/problems/string-compression/) | 1. [双指针](https://leetcode-cn.com/problems/string-compression/solution/ya-suo-zi-fu-chuan-by-leetcode/)，write 写原字符串，anchor锚定比较位，for read,c in enumerate(chars), read+1 表示后一位，c 表示当前位进行比较。 |
| 543  | [二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/) | 1.[递归](https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/)，左长，右长，交给递归来解决 |
| 560  | [和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/) | 1.遍历<br />2.前缀和，哈希表查找 prefix - k                  |
| 646  | [最长数对链](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/) | 1.先排序，后链接                                             |
| 680  | [验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/) | 1. [双指针](https://leetcode-cn.com/problems/valid-palindrome-ii/solution/yan-zheng-hui-wen-zi-fu-chuan-ii-by-leetcode-solut/)，先判断是否回文，如果不是，删除一个后，在给一次机会 |
| 718  | [最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/) | [官解](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/)<br />1.暴力，枚举A[i:]->B[j:], 遍历找公共前缀，取最大返回<br />2.DP，dp//[i]//[j], A[i:],B[j:]的最长公共前缀。若A[i]==B[j],则dp//[i]//[j] = dp//[i+1]//[j+1] + 1, 否则位0<br />3.滑动窗口，通过遍历对齐方式，然后得公共前缀<br />4.二分查找最大的连续公共子串，将特定长度的子串使用RK算法转换后存进hash表，然后从B的子串在A的hash表中对比查找，判断是否可以形成特定长度的公共子串 |
| 695  | [岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/) | [官解](https://leetcode-cn.com/problems/max-area-of-island/)<br />1.深度优先，递归，每次向四周搜索<br />2.深度优先，借助栈，尾部进来，尾部出append，pop<br />3.广度优先，借助deque, 尾部进来，头不出，popleft(), 如果是pop,就是深度优先了。 |
| 733  | [图像渲染](https://leetcode-cn.com/problems/flood-fill/)     | [官解](https://leetcode-cn.com/problems/flood-fill/solution/tu-xiang-xuan-ran-by-leetcode-solution/)<br />1. DFS<br />2. BFS |
| 739  | [每日温度](https://leetcode-cn.com/problems/daily-temperatures/) | 官解<br />1.暴力，反向遍历，字典维护每个温度第一次出现的位置，然后查找<br />2.栈，想出个遍历后，怎么想都想不出怎么优化,​ :pensive: |
| 785  | [判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/) | [官解](https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/)<br />1. DFS，遍历节点根据节点染色情况判断是否符合二分图<br />2. BFS |
|      |                                                              |                                                              |
| 836  | [矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap/) | [官解](https://leetcode-cn.com/problems/rectangle-overlap/solution/ju-xing-zhong-die-by-leetcode-solution/)<br />1.判断不重叠<br />2.投影，然后判断是否有交集`min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])` ,此公式IOU计算很有用 |
| 837  | [新21点](https://leetcode-cn.com/problems/new-21-game/)      | [官解](https://leetcode-cn.com/problems/new-21-game/solution/xin-21dian-by-leetcode-solution/)<br />1.动态规划，三种情况 [K,min(N,K+W-1)] -> 1, (min(N,K+W-1),K+W] -> 0，[0,K-1] -> dp[x] = 1/W*(dp(x+1) + ... + dp[x+W]), 然后差分优化<br />2. dp[K-1] = min(N - K + 1, W)/W, 刚开始概率为1的数量 |
| 912  | [排序数组](https://leetcode-cn.com/problems/sort-an-array/)  | 1.[归并排序，**分治算法**，子问题构建新的列表来存储结果](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247487045&idx=3&sn=e9f67f1fd33649c60478638c1d6cc2d9&key=86fce317de144aa641d25984adf4d5110a34d6995235ffcd431ddcfaf6b4aeb9037f4e236e4800d46e2c4f7a2c7cc05106593c207c59bf62ae295620cd7c3f3635d80d5092a9deb76305b5e1c7c7d728&ascene=1&uin=MzExOTA3MDE3Mw%3D%3D&devicetype=Windows+10&version=6208006f&lang=zh_CN&exportkey=A6HD67v3cF6uVv%2FgPHwimb0%3D&pass_ticket=nFXyKfVYsTU8JaGrP7IGX7STLom7%2F0YSXb6zJufgedmrCxEsPkmUcfANYDBwOUO8)<br />2.[**冒泡排序**，超时](https://www.youtube.com/watch?v=nmhjrI-aW5o)<br />3.[**快排**，找到中间数（pivot的左边都小于等于pivot的右边和pivot），左右分治](https://www.youtube.com/watch?v=COk73cpQbFQ)<br /> |
| 987  | [和可被 K 整除的子数组](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/) | 1. [前缀和](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/he-ke-bei-k-zheng-chu-de-zi-shu-zu-by-leetcode-sol/)同余原理，哈希表查 |
| 1014 | [最佳观光组合](https://leetcode-cn.com/problems/best-sightseeing-pair/) | 1.[枚举](https://leetcode-cn.com/problems/best-sightseeing-pair/solution/zui-jia-guan-guang-zu-he-by-leetcode-solution/)，然后根据公式优化从n2->n时间复杂度 |
| 1025 | [除数博弈](https://leetcode-cn.com/problems/divisor-game/)   | 1.[归纳法](https://leetcode-cn.com/problems/divisor-game/solution/python3gui-na-fa-by-pandawakaka/)，偶数必赢，奇数必输<br />2.[递归](https://leetcode-cn.com/problems/divisor-game/solution/chu-shu-bo-yi-by-leetcode-solution/) |
| 1028 | [从先序遍历还原二叉树](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/) | 1.[迭代](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/)，当前数字，是上一个节点的左子节点，或者是深度-1的根节点的右节点 |
| 1103 | [分糖果 II](https://leetcode-cn.com/problems/distribute-candies-to-people/) | 1.遍历，按规则一个一个发<br />2.[数学](https://leetcode-cn.com/problems/distribute-candies-to-people/solution/guan-jie-shu-xue-ji-suan-guo-cheng-by-haofengsiji/)，等差数列 |
|      |                                                              |                                                              |
| 1111 | [有效括号的嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) | [官解](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solution/you-xiao-gua-hao-de-qian-tao-shen-du-by-leetcode-s/)<br />1.栈，根据嵌套深度平均分<br />2.规律，左右括号有相应的奇偶分配规律 |
| 1160 | [拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/) | 1.构建字典表，查表                                           |
| 1371 | [每个元音包含偶数次的最长子字符串](https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) | 1.[前缀和](https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/python-jian-ji-piao-liang-you-dian-nan-li-jie-ban-/)，位操作（状态压缩） |

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

