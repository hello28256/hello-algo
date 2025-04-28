# -*-coding: utf-8 -*-
# @Time    : 2025/4/28 11:12
# @Author  : hello28256@gmail.com
# @FileName: Quick_Sort.py
# @Software: PyCharm
# @Blog    ：https://github.com/hello28256


class QuickSort:

    def partition(self, nums: list[int],left: int , right: int)->int:
        i,j = left,right
        while i<j:
            while i<j and nums[j]>=nums[left]:
                j-=1
            while i<j and nums[i]<=nums[left]:
                i+=1
            nums[i],nums[j]=nums[j],nums[i]
        nums[left],nums[i]=nums[i],nums[left]
        return i
    def quick_sort(self,nums:list[int],left:int,right:int)->list[int]:
        if left>=right:
            return
        pivot=self.partition(nums,left,right)
        self.quick_sort(nums,left,pivot-1)
        self.quick_sort(nums,pivot+1,right)

if __name__ == "__main__":
    # 快速排序
    nums = [2, 4, 7, 7, 3, 1, 6,1, 0, 3, 5]
    QuickSort().quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums =", nums)