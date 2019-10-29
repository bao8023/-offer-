# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# DFS
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    #  递归解法
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if root == None:
            return result

        self.sum = expectNumber
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if root.left == None and root.right == None and sum(path) == self.sum:
            result.append(path)
        if root.left != None:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right != None:
            self.DFS(root.right, result, path + [root.right.val])

    # 非递归解法
    # def FindPath(self, root, expectNumber):
    #     result=[]
    #     if root==None:
    #         return result
    #
    #     self.sum = expectNumber
    #
    #     stack=[]
    #     stack.append((root,[root.val]))
    #     while stack:
    #         node,path=stack.pop()
    #         if node.left==None and node.right==None and sum(path)==self.sum:
    #             result.append(path)
    #         if node.left!=None:
    #             stack.append((root.left,path+[root.left.val]))
    #         if node.right!=None:
    #             stack.append((root.right, path + [root.right.val]))
    #     return result