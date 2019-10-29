# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # if not pHead:
        #     return None
        #
        # dummy = pHead
        #
        # # first step, N' to N next
        # while dummy:
        #     dummynext = dummy.next
        #     copynode = RandomListNode(dummy.label)
        #     copynode.next = dummynext
        #     dummy.next = copynode
        #     dummy = dummynext  # 移动节点
        #
        # dummy = pHead
        #
        # # second step, random' to random'
        # while dummy:
        #     dummyrandom = dummy.random
        #     copynode = dummy.next
        #     if dummyrandom:
        #         copynode.random = dummyrandom.next
        #     dummy = copynode.next
        #
        # # third step, split linked list
        # dummy = pHead
        # copyHead = pHead.next  ##
        # while dummy:
        #     copyNode = dummy.next
        #     dummynext = copyNode.next
        #     dummy.next = dummynext
        #     if dummynext:
        #         copyNode.next = dummynext.next
        #     else:
        #         copyNode.next = None
        #     dummy = dummynext
        #
        # return copyHead

        # 递归法
        if not pHead:
            return
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode