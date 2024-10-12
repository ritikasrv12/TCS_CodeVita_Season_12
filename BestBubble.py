def merge_and_count(arr, temp_arr, left, right):
    if left == right:
        return 0
   
    mid = (left + right) // 2
    inv_count = 0
   
    inv_count += merge_and_count(arr, temp_arr, left, mid)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
   
    inv_count += merge(arr, temp_arr, left, mid, right)
   
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
   
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1) # Elements from arr[i] to arr[mid] are greater than arr[j]
            j += 1
        k += 1
   
    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
   
    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
   
    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
   
    return inv_count

def count_swaps(arr, ascending=True):
    n = len(arr)
    temp_arr = [0] * n
   
    if ascending:
        return merge_and_count(arr, temp_arr, 0, n - 1)
    else:
        arr = arr[::-1]  # Reverse the array to count swaps for descending order
        return merge_and_count(arr, temp_arr, 0, n - 1)

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Count swaps for ascending and descending order
ascending_swaps = count_swaps(arr.copy(), ascending=True)
descending_swaps = count_swaps(arr.copy(), ascending=False)

# Return the minimum number of swaps without any extra whitespace
print(min(ascending_swaps, descending_swaps), end="")
