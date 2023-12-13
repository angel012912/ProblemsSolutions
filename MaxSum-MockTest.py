from pprint import pprint

test = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
test1 = [[1, 3],[2,4]]

def maxSum(m):
    n = len(m) // 2
    sum = 0
    for i in range (n):
        for j in range (n):
            r1 = i
            r2 = len(m) - i - 1
            c1 = j
            c2 = len(m) - j - 1
            maximo = max(m[r1][c1], m[r2][c1], m[r1][c2], m[r2][c2])
            sum += maximo
    return sum

print(maxSum(test))