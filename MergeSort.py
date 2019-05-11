# Efficient for large data sets
# Divide and Conquer algorithm
# O(n log(n)) because each Merge step doubles the list size
# It does n work for each Merge step because it must look at every item
# for an example of 8 items log2of8 = 3(Merged Steps)


def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last+1]
    L.append(99999)  # presumably a large number
    R.append(99999)
    i = j = 0
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
