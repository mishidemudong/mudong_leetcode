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
        

        
        