# -*- coding:utf-8 -*-
class Solution:
    ''' method1: 提姆排序'''
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[: k]

    ''' method2: 快速排序'''
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x >= pivot])
            return left + [pivot] + right

        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[: k]