players = input().split()

record = {}
for player in players:
    if player not in record:
        record[player] = 1
    else:
        record[player] += 1

for key, value in record.items():
    if value == min(record.values()):
        print(key)
print(min(record.values()))