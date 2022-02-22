# 11720
from sympy import continued_fraction_reduce


n = int(input())
N = map(int, input())
print(sum(N))

# 2750
N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
sorted_num = sorted(num)
for i in range(len(num)):
    print(sorted_num[i])
    
# 2562
n_list = []
for i in range(1, 10):
    n_list.append(int(input()))
print(max(n_list))
print(n_list.index(max(n_list))+1)

# 1100
board = [list(input()) for row in range(8)]

result = 0

for i in range(8):
  for j in range(8):
    if (i+j)%2 == 0:
      if board[i][j] == "F":
        result += 1
print(result)

# 1032
num = int[input()]
file_n = [input() for _ in range(num)]
result = list(file_n[0])

for i in range(1, len(file_n)):
    for j in range(len(result)):
        if result[j] == "?":
            continue
        if result[j] != file_n[i][j]:
            result[j] = "?"
print("".join(result))
