"""

n array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

"""

def isMonotonic(A):
    return A == sorted(A) or A == sorted(A, reverse=True)

A = [1,2,2,3]
print(isMonotonic(A))
# Output: true
        