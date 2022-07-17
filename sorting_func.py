
import random
import time

# Sorting with a "Shell" algorithm
def shellSort(nums):
    n = len(nums)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = nums[i]
            j = i
            while j >= interval and nums[j - interval] > temp:
                nums[j] = nums[j - interval]
                j -= interval
            nums[j] = temp
        interval //= 2
    return nums

# Sorting with "merge" algorithm
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst 
        
def mergeSort(self, nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = self.mergeSort(nums[:mid+1])
    lst2 = self.mergeSort(nums[mid+1:])
    result = self.merge(lst1, lst2)
    return result

# Sorting with "quick sort" algorithm
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


a=[]
rand_numbers = 1000
arrange_numbers = rand_numbers/5
for i in range(rand_numbers):
    a.append(random.randint(0, 1000000))
for i in range(arrange_numbers):
    a.append(i)
print("Array is ready. There are " + str(rand_numbers+arrange_numbers) + " elements in array.")

# t0 = time.clock()
# shellSort(a)
# t = time.clock() - t0
# print("Shell Sort time is ", t)

# t0 = time.clock()
# mergeSort(a)
# t = time.clock() - t0
# print("Merge Sort time is ", t)

# t0 = time.clock()
# quick_sort(a)
# t = time.clock() - t0
# print("Quick Sort time is ", t)

t0 = time.clock()
a.sort()
t = time.clock() - t0
print("Default Sort time is ", t)