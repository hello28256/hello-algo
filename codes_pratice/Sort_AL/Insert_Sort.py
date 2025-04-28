# -*-coding: utf-8 -*-
# @Time    : 2025/4/28 15:06
# @Author  : hello28256@gmail.com
# @FileName: Insert_Sort.py
# @Software: PyCharm
# @Blog    ：https://github.com/hello28256






def insertion_sort(nums:list[int]):
    #升序
    for i in range(1,len(nums)):
        base = nums[i]
        j = i-1
        while j>=0 and nums[j]>base:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]= base

"""Driver Code"""
if __name__ == "__main__":
    nums = [6, 4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("插入排序完成后 nums =", nums)