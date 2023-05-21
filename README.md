# LeetCode
Leet's Grind

1.  [Two Sum](#two-sum)
2.  [Add Two Numbers](#add-two-numbers)
2130. [Maximum Twin Sum of a Linked List](#maximum-twin-sum-of-a-linked-list)

---

### [[0001] Two Sum](https://leetcode.com/problems/two-sum/)<a name="two-sum"></a>
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        codex = {}
        for i, n in enumerate(nums):
            if target - n in codex:
                return [codex[target - n], i]
            codex[n] = i
        return codex
```

### [[0002] Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)<a name="add-two-numbers"></a>
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = head = ListNode(0)
        carry = 0
        while (l1 or l2 or carry):
            sumVal = carry
            if l1:
                sumVal += l1.val
                l1 = l1.next
            if l2:
                sumVal += l2.val
                l2 = l2.next
            carry = sumVal // 10
            current.next = ListNode(sumVal % 10)
            current = current.next
        return head.next
```

### [[2130] Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)<a name="maximum-twin-sum-of-a-linked-list"></a>
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        """
        # Solution 1 | Two Pointers with Array
        # Runtime: O(N) | Memory: O(N)
        # Algorithm: traverse linked list, two pointers meeting inwards,
        # track and return max twin sum
        current = head
        convert = []
        while(current):
            convert.append(current.val)
            current = current.next
        for i in range(len(convert) // 2):
            convert[i] += convert[len(convert) - 1 - i]
        return max(convert)
        """

        # Solution 2 | Two Pointers with Linked List
        # Runtime: O(N) | Memory: O(1)
        # Algorithm: first pass: traverse linked list and reverse the first half,
        # second pass: traverse linked list, tracking maxTwinSum
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        maxTwinSum = 0
        while slow and prev:
            maxTwinSum = max(slow.val + prev.val, maxTwinSum)
            slow = slow.next
            prev = prev.next
        return maxTwinSum
```
---
