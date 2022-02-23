n = int(input())
co_cap = {}
for i in range(n):
    ent = input().split()
    co_cap[ent[0]] = ent[1]

a = input()    
print(co_cap.get(a, "Unknown Country"))