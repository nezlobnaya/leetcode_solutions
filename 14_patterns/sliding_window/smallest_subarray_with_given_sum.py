def smallest_subarray_with_given_sum(s, arr):
  min_length,window_sum, window_start =float('inf'),0,0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum>=s:
      min_length = min(min_length, window_end-window_start +1)
      window_sum -=arr[window_start]
      window_start+=1


  return 0 if min_length == float('inf') else min_length

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
