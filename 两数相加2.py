# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:17:46 2021

@author: Administrator
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a1, a2 = [], []
    
    while l1.next:
        a1.append(l1.val)
        l1 = l1.next
    
    while l2.next:
        a2.append(l2.val)
        l2 = l2.next
        
    jinwei = 0
    
    length = max([len(a1),len(a2)])
    ans = None
    while length > 0:
        
        num1 = 0 if a1==[] else a1.pop() 
        num2 = 0 if a2==[] else a2.pop()
        total = num1 + num2 + jinwei

        if total >= 10:
            jinwei = 1
        else:
            jinwei = 0
            
        current = total % 10

        node = ListNode(current)
        node.next = ans
        ans = node
        
        length -= 1
        
    return ans


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []

        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        ans = None
        jinwei = 0

        while l1_list or l2_list or jinwei != 0:
            if l1_list:
                a = l1_list.pop()
            else:
                a = 0

            if l2_list:
                b = l2_list.pop()
            else:
                b = 0

            curr = a + b + jinwei
            jinwei = curr // 10
            curr = curr % 10

            currnode = ListNode(curr)
            currnode.next = ans
            ans = currnode

        return ans

        # s1, s2 = [], []
        # while l1:
        #     s1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     s2.append(l2.val)
        #     l2 = l2.next
        # ans = None
        # carry = 0
        # while s1 or s2 or carry != 0:
        #     a = 0 if not s1 else s1.pop()
        #     b = 0 if not s2 else s2.pop()
        #     cur = a + b + carry
        #     carry = cur // 10
        #     cur %= 10
        #     curnode = ListNode(cur)
        #     curnode.next = ans
        #     ans = curnode
        # return ans
        

        
        