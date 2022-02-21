print("hello world")
# 1000번
a, b = map(int, input().split())
print(a+b)

# 2558
a = int(input())
b = int(input())
print(a+b)

# 10950 
for i in range(int(input())):
    a, b = map(int, input().split())
    print(a+b)
    
# 10953
for i in range(int(input())):
    a, b = map(int, input().split(","))
    print(a+b)
    
# 11021
for i in range(int(input())):
    a,b = map(int,input().split())
    print(f"Case #{i+1}: ",a+b)
    
# 11022
for i in range(int(input())):
      a, b = map(int, input().split())
      print(f"Case #{i+1}: {a} + {b} = {a+b}")
    
# 2438
for i in range(int(input())):
      print("*"*(i+1))
      

# 2439
A = int(input())
for i in range(1, A+1):
    print(" "*(A-i),"*"*i)
    
# 10995
A = int(input())
if A == 1:
    print("*")
else:
    for i in range(A):
        if i % 2 == 0:
            print("* "*A)
        else:
            print(" *"*A)
            

# 10988
a = input()
if a == a[::-1]:
    print(1)
else:
    print(0)
    
# 2711
n = int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)
    print(b[:a-1],b[a:],sep="")
    
# 17249
p = str(input())
a = p.split("(^0^)")
print(a[0].count("@", a[1].count("@")))

# 2789
mail = input()
for i in "CAMBRIDGE":
    mail = mail.replace(i, "")
print(mail)

# 2675
T = int(input())
for i in range(T):
    R, S = input().split()
    text = ""
    for i in S:
        text += int(R)*i
    print(text)

# 2941
C = ["c=","c-","dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
for i in C:
    a = a.replace(i, "1")
print(len(a))

# 8892
T = int(input())
for i in range(T):
    k = int(input())
    word = []
    for i in range(k):
        w = input()
        word.append(w)
        
    li = []
    pal = []
    for i in range(len(word)):
        for j in range(len(word)):
            if i == j:
                pass
            else:
                a = word[i] + word[j]
                li.append(a)
                pal.append(a[::-1])
    result = []
    for i in range(len(li)):
        if li[i] == pal[i]:
            result.append(li[i])
    if len(result) ==0:
        print(0)
    else:
        print(result[0])
        

# 2804
A, B = map(str, input().split())
for i in range(len(A)):
    if A[i] in B:
        M = i
        N = B.index(A[i])
        break
for j in range(len(B)) :
    if j == N:
        print(A)
    else:
        print("."*M +B[j]+"."*(len(A)-M-1))