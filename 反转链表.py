#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:18 2021

@author: liang
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):

    reverse = None
    tail = head

    while tail.next:
        # reverse = head
        # tail.next = head.next

        reverse, tail.next, tail=tail, reverse, tail.next

    return reverse
