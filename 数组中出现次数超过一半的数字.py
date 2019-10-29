# -*- coding:utf-8 -*-
class Solution:
    ''' 第一种，用python的标准库collections '''
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2.0:
            return count[0][0]
        return 0

class Solution:
    ''' 第二种方法：dict来计数 '''
    def MoreThanHalfNum_Solution(self, numbers):
        dict = {}
        for no in numbers:
            if not dict.get(no):
                dict[no] = 1
            else:
                dict[no] = dict[no] + 1
            if dict[no] > len(numbers)/2:
                return no
        return 0