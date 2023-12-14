"""
Given an array of distinct elements. Let M1 and M2 be the smallest and the next smallest element in the interval [L, R] where 1 <= L < R <= N.

Given
Si = ((M1 AND M2) XOR (M1 OR M2)) AND (M1 XOR M2)

Find the maximum possible value of Si.


Example:

Input: arr[] = {10, 20, 30, 40, 50}
Output: 48
Explanation:
M1 and M2 are 30 and 40 respectively.

"""


def findMax(arr):
    n = len(arr)
    max_val = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            m1 = min(arr[i], arr[j])
            m2 = max(arr[i], arr[j])
            val = ((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2)
            max_val = max(max_val, val)
    return max_val

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(findMax(arr))

