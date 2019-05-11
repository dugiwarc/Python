def bubbleSort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


print(bubbleSort([1, 4, 5, 2, 8, -1, 3, 5, 2]))
