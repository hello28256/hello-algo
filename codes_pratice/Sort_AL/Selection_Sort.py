# -*-coding: utf-8 -*-
# @Time    : 2025/4/28 11:46
# @Author  : hello28256@gmail.com
# @FileName: Selection_Sort.py
# @Software: PyCharm
# @Blog    ：https://github.com/hello28256




def selection_sort(nums:list[int]):
    # 选择排序，如果是递增，第一遍先记录最小的数，然后与第一位数进行交换
    n = len(nums)
    #nums=[1,2,3,4,5]
    for i in range(n-1):#i [0,1,2,3]
        k=i
        for j in range(i+1,n):#[i+1,n]
            if nums[j]<nums[k]:
                k=j
        nums[i],nums[k]=nums[k],nums[i]


if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2, 5, 3, 5, 6, 2]
    selection_sort(nums)
    print("选择排序完成后 nums =", nums)