"""
this file contains some of the most popular sorting algorithms:
    bubble sort, insertion sort, selection sort, merge sort, quick sort, heap sort
    radix sort, counting sort, bucket sort, shell sort, comb sort
    cycle sort, cocktail sort, gnome sort, and pancake sort

created by:
Jased#0001
and Github Copilot
"""

if __name__ == "__main__":
    exit()

#bubble sort, insertion sort, selection sort, merge sort, quick sort, and heap sort
def bubble(sort: list):
    """
    bubble sort algorithm
    """
    try:
        for i in range(len(sort)):
            for j in range(len(sort)-1):
                if sort[j] > sort[j+1]:
                    sort[j], sort[j+1] = sort[j+1], sort[j]
        return sort
    except Exception as e:
        return e

def insertion(sort: list):
    """
    insertion sort algorithm
    """
    try:
        for i in range(1, len(sort)):
            j = i
            while j > 0 and sort[j-1] > sort[j]:
                sort[j-1], sort[j] = sort[j], sort[j-1]
                j -= 1
        return sort
    except Exception as e:
        return e

def selection(sort: list):
    """
    selection sort algorithm
    """
    try:
        for i in range(len(sort)):
            min = i
            for j in range(i+1, len(sort)):
                if sort[min] > sort[j]:
                    min = j
            sort[i], sort[min] = sort[min], sort[i]
        return sort
    except Exception as e:
        return e

def merge(sort: list):
    """
    merge sort algorithm
    """
    try:
        if len(sort) > 1:
            mid = len(sort)//2
            left = sort[:mid]
            right = sort[mid:]
            merge(left)
            merge(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sort[k] = left[i]
                    i += 1
                else:
                    sort[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                sort[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                sort[k] = right[j]
                j += 1
                k += 1
        return sort
    except Exception as e:
        return e

def quick(sort: list):
    """
    quick sort algorithm
    """
    try:
        if len(sort) > 1:
            pivot = sort[0]
            left = []
            right = []
            for i in range(1, len(sort)):
                if sort[i] < pivot:
                    left.append(sort[i])
                else:
                    right.append(sort[i])
            quick(left)
            quick(right)
            sort[:] = left + [pivot] + right
        return sort
    except Exception as e:
        return e

def heap(sort: list):
    """
    heap sort algorithm
    """

    def heapify(arr: list, n: int, i: int):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    try:
        n = len(sort)
        for i in range(n, -1, -1):
            heapify(sort, n, i)
        for i in range(n-1, 0, -1):
            sort[i], sort[0] = sort[0], sort[i]
            heapify(sort, i, 0)
        return sort
    except Exception as e:
        return e

#radix sort, counting sort, bucket sort, shell sort, and comb sort
def radix(sort: list):
    """
    radix sort algorithm
    """
    try:
        max = 0
        for i in range(len(sort)):
            if max < sort[i]:
                max = sort[i]
        for i in range(1, max+1):
            bucket = [[] for i in range(10)]
            for j in range(len(sort)):
                bucket[sort[j]%10].append(sort[j])
            sort = []
            for j in range(10):
                sort += bucket[j]
        return sort
    except Exception as e:
        return e

def counting(sort: list):
    """
    counting sort algorithm
    """
    try:
        max = 0
        for i in range(len(sort)):
            if max < sort[i]:
                max = sort[i]
        count = [0]*(max+1)
        for i in range(len(sort)):
            count[sort[i]] += 1
        for i in range(1, max+1):
            count[i] += count[i-1]
        for i in range(len(sort)-1, -1, -1):
            sort[count[sort[i]]-1] = sort[i]
            count[sort[i]] -= 1
        return sort
    except Exception as e:
        return e

def bucket(sort: list):
    """
    bucket sort algorithm
    """
    try:
        max = 0
        for i in range(len(sort)):
            if max < sort[i]:
                max = sort[i]
        bucket = [[] for i in range(max+1)]
        for i in range(len(sort)):
            bucket[sort[i]].append(sort[i])
        sort = []
        for i in range(max+1):
            sort += bucket[i]
        return sort
    except Exception as e:
        return e

def shell(sort: list):
    """
    shell sort algorithm
    """
    try:
        gap = len(sort)//2
        while gap > 0:
            for i in range(gap, len(sort)):
                temp = sort[i]
                j = i
                while j >= gap and sort[j-gap] > temp:
                    sort[j] = sort[j-gap]
                    j -= gap
                sort[j] = temp
            gap //= 2
        return sort
    except Exception as e:
        return e

def comb(sort: list):
    """
    comb sort algorithm
    """
    try:
        gap = len(sort)
        while gap > 1:
            gap = int(gap/1.3)
            for i in range(gap, len(sort)):
                temp = sort[i]
                j = i
                while j >= gap and sort[j-gap] > temp:
                    sort[j] = sort[j-gap]
                    j -= gap
                sort[j] = temp
        return sort
    except Exception as e:
        return e
        
#cycle sort, cocktail sort, gnome sort, and pancake sort
def cycle(sort: list):
    """
    cycle sort algorithm
    """
    try:
        for i in range(len(sort)):
            while i > 0 and sort[i] < sort[i-1]:
                sort[i], sort[i-1] = sort[i-1], sort[i]
                i -= 1
        return sort
    except Exception as e:
        return e

def cocktail(sort: list):
    """
    cocktail sort algorithm
    """
    try:
        left = 0
        right = len(sort)-1
        while left < right:
            for i in range(left, right):
                if sort[i] > sort[i+1]:
                    sort[i], sort[i+1] = sort[i+1], sort[i]
            right -= 1
            for i in range(right, left, -1):
                if sort[i] < sort[i-1]:
                    sort[i], sort[i-1] = sort[i-1], sort[i]
            left += 1
        return sort
    except Exception as e:
        return e

def gnome(sort: list):
    """
    gnome sort algorithm
    """
    try:
        i = 0
        while i < len(sort):
            if i == 0 or sort[i] >= sort[i-1]:
                i += 1
            else:
                sort[i], sort[i-1] = sort[i-1], sort[i]
                i -= 1
        return sort
    except Exception as e:
        return e

def pancake(sort: list):
    """
    pancake sort algorithm
    """
    try:
        for i in range(len(sort)):
            for j in range(i, len(sort)):
                if sort[j] < sort[i]:
                    sort[j], sort[i] = sort[i], sort[j]
                    if i != 0:
                        sort[:i+1] = sort[:i+1][::-1]
                    if j != len(sort)-1:
                        sort[j+1:] = sort[j+1:][::-1]
        return sort
    except Exception as e:
        return e