'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import sys
INT_MIN = -sys.maxsize -1
def sliding_window_max(arr, nums, k):
    # Your code here
    sliding_window_max = INT_MIN
    for i in range(nums - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
            maxsum = max(current_sum, maxsum)
        return maxsum



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    nums = len(arr)

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, nums, k)}")
