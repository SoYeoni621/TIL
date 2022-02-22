# 921
n = int(input())
num_list = [i**2 for i in range(1, n+1)]
print(num_list)

# 929
n = int(input())
num_list = [f"No.{i}" for i in range(1, n+1) ]
print(num_list)

# 926
import numpy as np

arr = [list(map(int, input().split())) for row in range(2)]
arr2 = [list(map(int, input().split())) for row in range(2)]

result = np.multiply(arr, arr2)
print(result)