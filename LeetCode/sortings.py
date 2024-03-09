def selection(array):
    size = len(array)
    for ind in range(size):
        swapped = False
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
                swapped = True
        if swapped:
            array[ind], array[min_index] = array[min_index], array[ind]

    return array


def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key

    return array


def merge(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge(L)
        merge(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

    return array


# function to perform quicksort
def quickSort(array, low, high):
    # function to find the partition position
    def partition(array, low, high):
        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # return the position from where partition is done
        return i + 1

    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)
    return array







