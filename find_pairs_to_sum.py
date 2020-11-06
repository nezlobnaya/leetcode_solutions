"""
Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
"""


# we need to loop through the array
# check the every pair of integers
# return all pairs which sum up to S 
# creating a new array

# def pair_integers(arr, S):
#   result = []
#   hash = {}
#   for i in range(len(arr)):
#     element = S - arr[i]
#     if element in hash:
#       result.append([arr[i], element])
#     else:
#       hash[arr[i]] = arr[i]
#   return result[::-1]
 



def pair_integers(arr, S):
  result = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == S:
            result.append([arr[j], arr[i]])
        # else:
        #     return None
  return result[::-1]

arr = [3, 5, 2, -4, 8, 11]
S = 7

print(pair_integers(arr, S))
#  output [[11, -4], [2, 5]]