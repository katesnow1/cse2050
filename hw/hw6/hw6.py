def bubble_sort(matrix):
    """sorts the first row of param matrix using bubble sort"""
    matrix_row1 = matrix[0]
    n_swaps = 0
    n = len(matrix_row1)

    ISSORTED = False
    j = 0
    while not ISSORTED:

        ISSORTED = True
        for i in range(n-1-j):
            if matrix_row1[i] > matrix_row1[i+1]:
                ISSORTED = False
                matrix_row1[i], matrix_row1[i+1] = matrix_row1[i+1], matrix_row1[i]
                n_swaps+=1
        j+=1
    return matrix_row1, n_swaps

def insertion_sort(matrix):
    """sorts the second row of param matrix using insertion sort"""
    n_swaps = 0
    matrix_row2 = matrix[1]
    n = len(matrix_row2)
    for i in range(n-1):
        j = n-2-i
        item = matrix_row2[j]

        while j < n-1 and item > matrix_row2[j+1]:
            matrix_row2[j] = matrix_row2[j+1]
            n_swaps+=1
            j+=1
        
        matrix_row2[j] = item
    
    return matrix_row2, n_swaps

def selection_sort(matrix):
    """sorts the third row of param matrix using selection sort"""
    n_swaps = 0
    matrix_row3 = matrix[2]
    n = len(matrix_row3)
    for i in range(n-1):
        idx_max = n-i-1
        item_max = matrix_row3[idx_max]
        swapped = False

        for j in range(n-i):
            if matrix_row3[j] > item_max:
                swapped = True
                idx_max = j
                item_max = matrix_row3[idx_max]
        
        if swapped:
            matrix_row3[idx_max], matrix_row3[j] = matrix_row3[j], matrix_row3[idx_max]
            n_swaps += 1

    return matrix_row3, n_swaps

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list


if __name__ == '__main__':
    #L = [[1,5,23,69,2,0,35,5,7,9], [1,5,23,69,2,0,35,5,7,9], [1,5,23,69,2,0,35,5,7,9]]
    L = [[10, 9, 8,7,6,5,4,3,2,1],[10, 9, 8,7,6,5,4,3,2,1],[10, 9, 8,7,6,5,4,3,2,1]]
    print(selection_sort(L))