# Insertion Sort uses nested loops to sort O(n^2)
# Useful only for small data sets n < 1k
# Expensive operation is swapping ( 3 operations take place )


def insertion_sort_sw(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A


# print(insertion_sort([1, 4, 5, 2, 8, -1, 3, 5, 2]))

# Insertion Sort using a shifting method
def insertion_sort_sh(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i - 1, -1, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
    return A


print(insertion_sort_sh([1, 4, 5, 2, 8, -1, 3, 5, 2]))
