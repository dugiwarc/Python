# Selection sort is not a fast sorting algorithm because it uses nested loops
# Useful only for small data sets
# It runs in O(n^2)


def selection_sort(A):
    for i in range(len(A) - 1):
        min_val = A[i]
        for j in range(i+1, len(A)):
            if(A[j] < min_val):
                min_val = A[j]
                A[j] = A[i]
                A[i] = min_val
    return A


print(selection_sort([1, 4, 5, 2, 8, -1, 3, 5, 2]))
