# Data Scientist Algo Problems in Python

Basic-to-Medium level of algorithm solving skill is playing a more and more important role in Data Scientist work nowadays. But many DS may find it's hard to pick up LeetCode questions, plus, many questions are indeed irrevalent to data analytical work. 

To effectively improve coding skills as a DS, I am summerizing the most revanlent algorithm and data structure problems in this repo with notes. The topic covers Array, Strings, List, Matrix, (binary) Sorting & Searching, Math as well as selected Dynamic Programming problems.

I hope visitors can find this is useful! :raised_hands:

# **Data Structure**
### Binary Tree
Pre-order: root, left, right
In-order: left, root, right
Post-order: left, right, root

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [114. latten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List.py)|post-order|
| [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node.py)|pre-order|
| [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/226.%20Invert%20Binary%20Tree.py)|pre or post|
| [654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/654.%20Maximum%20Binary%20Tree.py)|pre-order|
|[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.py)|pre-order|
|[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal.py)|pre-order|
| [889. Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/889.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Postorder%20Traversal.py)|pre-order|
| [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/652.%20Find%20Duplicate%20Subtrees.py)|post-order|
| [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)| Hard | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/297.%20Serialize%20and%20Deserialize%20Binary%20Tree.py)|pre or post|
| [1373. Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)| Hard | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/1373.%20Maximum%20Sum%20BST%20in%20Binary%20Tree.py)|post-order|
| [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)| Easy | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree.py)|post-order|
| [669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)| Medium | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/669.%20Trim%20a%20Binary%20Search%20Tree.py)|pre-order|
| [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)| Easy | [Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Binary%20Tree/543.%20Diameter%20of%20Binary%20Tree.py)|post-order|

### Binary Search Tree (BST)

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/230.%20Kth%20Smallest%20Element%20in%20a%20BST.py)|in-order|
| [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/538.%20Convert%20BST%20to%20Greater%20Tree.py)|in-order|
| [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/700.%20Search%20in%20a%20Binary%20Search%20Tree.py)|BST search|
| [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/450.%20Delete%20Node%20in%20a%20BST.py)|BST delete|
| [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/701.%20Insert%20into%20a%20Binary%20Search%20Tree.py)|BST insert|
| [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/98.%20Validate%20Binary%20Search%20Tree.py)|BST verify|
| [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/96.%20Unique%20Binary%20Search%20Trees.py)|BST + DP|
| [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/BST/95.%20Unique%20Binary%20Search%20Trees%20II.py)||


### Graph

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/797.%20All%20Paths%20From%20Source%20to%20Target.py)|graph traverse|
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/207.%20Course%20Schedule.py)|graph traverse|
| [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/210.%20Course%20Schedule%20II.py)|topological order|
| [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/785.%20Is%20Graph%20Bipartite%3F.py)|DFS|
| [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/886.%20Possible%20Bipartition.py)|DFS|
| [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph.py)|Union-Find|
| [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/990.%20Satisfiability%20of%20Equality%20Equations.py)|Union-Find|
| [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/261.%20Graph%20Valid%20Tree.py)|Kruskal|
| [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/1135.%20Connecting%20Cities%20With%20Minimum%20Cost.py)|MST-Kruskal|
| [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/1584.%20Min%20Cost%20to%20Connect%20All%20Points.py)|MST-Kruskal|
| [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/743.%20Network%20Delay%20Time.py)|Dijkstra+PQ|
|[1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/1631.%20Path%20With%20Minimum%20Effort.py)|Dijkstra variant|
|[1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/1514.%20Path%20with%20Maximum%20Probability.py)|Dijkstra variant|
|[277. Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) | Medium |[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Graph/277.%20Find%20the%20Celebrity.py)||


### Array

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py)
| [289. Rotate Array](https://leetcode.com/problems/rotate-array/) | |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/189.%20Rotate%20Array.py)
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/217.%20Contains%20Duplicate.py)
| [136. Single Number](https://leetcode.com/problems/single-number/) | |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/136.%20Single%20Number.py)
| [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) || [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/350.%20Intersection%20of%20Two%20Arrays%20II.py)
| [66. Plus One](https://leetcode.com/problems/plus-one/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/66.%20Plus%20One.py)
| [1. Two Sum](https://leetcode.com/problems/two-sum/) |Easy|  [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/1.%20Two%20Sum.py)
| [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py)
| [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/15.%203Sum.py)
| [18. 4Sum](https://leetcode.com/problems/4sum/) | Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/18.%204Sum.py)|generic nSum solution|
| [163. Missing Ranges](https://leetcode.com/problems/missing-ranges/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/163.%20Missing%20Ranges.py)
| [36. Valid Sudoku](https://leetcode.com/problems/missing-ranges/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/163.%20Missing%20Ranges.py)
| [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/48.%20Rotate%20Image.py)
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/49.%20Group%20Anagrams.py)
| [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/303.%20Range%20Sum%20Query%20-%20Immutable.py)|presum Cache|
| [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/560.%20Subarray%20Sum%20Equals%20K.py)|presum cache + dict|
| [370. Range Addition](https://leetcode.com/problems/range-addition/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/370.%20Range%20Addition.py)|array diff cache|
| [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/1109.%20Corporate%20Flight%20Bookings.py)|array diff cache|
| [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/1109.%20Corporate%20Flight%20Bookings.py)|array diff cache|
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  |Hard| [My Solution]()|Sliding window|
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py)|Sliding window|
| [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/567.%20Permutation%20in%20String.py)|Sliding window|
| [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)  |Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/438.%20Find%20All%20Anagrams%20in%20a%20String.py)|Sliding window|



### Strings

| Problem No.      | Problem Name          |  Question  | Solution  |
| ------------- |:-------------| :-----:| :-----:|
| 344     | Reverse String | [LC Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/344.%20Reverse%20String.py)
| 7     | Reverse Integer | [LC Link](https://leetcode.com/problems/reverse-integer/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/7.%20Reverse%20Integer.py)
| 387   | First Unique Character in a String | [LC Link](https://leetcode.com/problems/first-unique-character-in-a-string/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/387.%20First%20Unique%20Character%20in%20a%20String.py)
| 242   | Valid Anagram | [LC Link](https://leetcode.com/problems/valid-anagram/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/242.%20Valid%20Anagram.py)
| 125   | Valid Palindrome | [LC Link](https://leetcode.com/problems/valid-palindrome/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/125.%20Valid%20Palindrome.py)
| 8   | String to Integer (atoi) | [LC Link](https://leetcode.com/problems/string-to-integer-atoi/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/8.%20String%20to%20Integer%20\(atoi\).py)
| 28   | Implement strStr() | [LC Link](https://leetcode.com/problems/implement-strstr/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/28.%20Implement%20strStr\(\).py)
| 14   |  Longest Common Prefix | [LC Link](https://leetcode.com/problems/longest-common-prefix/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/14.%20Longest%20Common%20Prefix.py)



### Linked List


|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/%23%20Two%20pointers.py)|Two pointers, dummy head|
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/23.%20Merge%20k%20Sorted%20Lists.py)|PriorityQueue, pointer, dummy head|
| [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/19.%20Remove%20Nth%20Node%20From%20End%20of%20List.py)|Slow and fast pointers|
| [876. Middle of the Linked List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/876.%20Middle%20of%20the%20Linked%20List.py)|Slow and fast pointers|
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.py)|Slow and fast pointers|
| [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/142.%20Linked%20List%20Cycle%20II.py)|Slow and fast pointers|
| [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/160.%20Intersection%20of%20Two%20Linked%20Lists.py)|Two pointers|
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/206.%20Reverse%20Linked%20List.py)|Recursive|
| [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/92.%20Reverse%20Linked%20List%20II.py)|Recursive twice|



### Matrix

| Problem No.      | Problem Name          | Difficulty|Question  | Solution  | Comment |
| ------------- |:-------------|:-------------:| :-----:| :-----:|:-----:|
| 73     | Set Matrix Zeroes |Easy| [LC Link](https://leetcode.com/problems/set-matrix-zeroes/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Matrix/73.%20Set%20Matrix%20Zeroes.py)
| 304     | Range Sum Query 2D - Immutable |Medium| [LC Link](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Matrix/304.%20Range%20Sum%20Query%202D%20-%20Immutable.py)|2D version of [303](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Array/303.%20Range%20Sum%20Query%20-%20Immutable.py)|


### Stack/Queue


|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/232.%20Implement%20Queue%20using%20Stacks.java)||
| [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/225.%20Implement%20Stack%20using%20Queues.java)||
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/20.%20Valid%20Parentheses.py) ||
| [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/921.%20Minimum%20Add%20to%20Make%20Parentheses%20Valid.py)||
| [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/1541.%20Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String.py)||
| [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/496.%20Next%20Greater%20Element%20I.py)| Monotonic Stack: value|
| [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/739.%20Daily%20Temperatures.py)| Monotonic Stack: index|
| [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/503.%20Next%20Greater%20Element%20II.py)| Monotonic Stack: circular|
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/239.%20Sliding%20Window%20Maximum.py)| Monotonic Queue, deque|
| [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/316.%20Remove%20Duplicate%20Letters.py)| Monotonic stack|
| [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) | Medium|[Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Stack%20Queue/1081.%20Smallest%20Subsequence%20of%20Distinct%20Characters.py)| Monotonic stack|


# **Algorithm**

### Sorting and Searching

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
|[88. Merge Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/88.%20Merge%20Sorted%20Array.py) ||
|[278. First Bad Version](https://leetcode.com/problems/first-bad-version/) | | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/278.%20First%20Bad%20Version.py) ||
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/704.%20Binary%20Search.py) |Binary search|
| [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.py) |binary search|
| [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/875.%20Koko%20Eating%20Bananas.py) |binary search|
| [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Sorting%20and%20Searching/1011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.py) |binary search|


### Two Pointers
|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
|[870. Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Two%20Pointers/870.%20Advantage%20Shuffle.py) ||
|[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  | Easy| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Two%20Pointers/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py)|Slow/Fast pointers|
|[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)  | Easy| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Two%20Pointers/83.%20Remove%20Duplicates%20from%20Sorted%20List.py)|Slow/Fast pointers|
|[27. Remove Element](https://leetcode.com/problems/remove-element/)  | Easy| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Two%20Pointers/27.%20Remove%20Element.py)|Slow/Fast pointers|
|[283. Move Zeros](https://leetcode.com/problems/move-zeroes/) | Easy| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Two%20Pointers/283.%20Move%20Zeroes.py)|Slow/Fast pointers|

### DFS BFS
|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/DFS_BFS/46.%20Permutations.py)|deep copy of attr lst|
| [77. Combinations](https://leetcode.com/problems/combinations/) | Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/DFS_BFS/77.%20Combinations.py)|deep copy of attr lst|

### Math
|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/412.%20Fizz%20Buzz.py)||
| [204. Count Primes](https://leetcode.com/problems/count-primes/) |Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/204.%20Count%20Primes.py)||
| [231. Power of Two](https://leetcode.com/problems/power-of-two/) |Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/231.%20Power%20of%20Two.py)||
| [326. Power of Three](https://leetcode.com/problems/power-of-three/) |Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/326.%20Power%20of%20Three.py)||
| [342. Power of Four](https://leetcode.com/problems/power-of-four/) |Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/342.%20Power%20of%20Four.py)||
| [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/13.%20Roman%20to%20Integer.py)||
| [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) |Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/172.%20Factorial%20Trailing%20Zeroes.py)||
| [793. Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) |Hard | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/793.%20Preimage%20Size%20of%20Factorial%20Zeroes%20Function.py)||
| [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) |Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/382.%20Linked%20List%20Random%20Node.py)||
| [398. Random Pick Index](https://leetcode.com/problems/random-pick-index/) |Medium | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/398.%20Random%20Pick%20Index.py)||
| [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/) |Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Math/645.%20Set%20Mismatch.py)||


### Dynamic Programming

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |Easy |[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Dynamic%20Programming/70.%20Climbing%20Stairs.py)||

### Divide and Conquer

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Divide%20and%20Conquer/241.%20Different%20Ways%20to%20Add%20Parentheses.py)||

### Recursion

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [344. Reverse String](https://leetcode.com/problems/merge-sorted-array/) | Easy | [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Strings/344.%20Reverse%20String.py)||
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Linked%20List/206.%20Reverse%20Linked%20List.py)|Recursive|


### Others

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
| [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) |Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/118.%20Pascal's%20Triangle.py)||
| [268. Missing Number](https://leetcode.com/problems/missing-number/) |Easy|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/268.%20Missing%20Number.py)||
| [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/1288.%20Remove%20Covered%20Intervals.py)|intervals|
| [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/56.%20Merge%20Intervals.py)|intervals|
| [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/986.%20Interval%20List%20Intersections.py)|intervals|
| [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium|[My Solution](https://leetcode.com/problems/kth-largest-element-in-an-array/)|PQ|
| [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/253.%20Meeting%20Rooms%20II.py)|intervals|
| [1024. Video Stitching](https://leetcode.com/problems/video-stitching/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/1024.%20Video%20Stitching.py)|interval|
| [134. Gas Station](https://leetcode.com/problems/gas-station/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/134.%20Gas%20Station.py)||
| [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/224.%20Basic%20Calculator.py)||
| [659. Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Medium|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/659.%20Split%20Array%20into%20Consecutive%20Subsequences.py)||
| [391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/) | Hard|[My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Others/391.%20Perfect%20Rectangle.py)||



### Data Structure Design

|Problem Name  | Difficulty    | Solution  | Comment |
|:-------------|:-------------:| :--------:|:-----:|
|[146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Data%20Structure%20Design/146.%20LRU%20Cache.py) |OrderedDict()/LinkedHashMap<>()|
|[380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python) |list + map: O(1) swap|
|[710. Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) | Hard| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Data%20Structure%20Design/710.%20Random%20Pick%20with%20Blacklist.py) | dict to map the backlist|
|[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard| [My Solution](https://github.com/stellapeng/Data-Scientist-Algo-Problems-in-Python/blob/main/Data%20Structure%20Design/295.%20Find%20Median%20from%20Data%20Stream.java) | PriorityQueue, heapq in python|




