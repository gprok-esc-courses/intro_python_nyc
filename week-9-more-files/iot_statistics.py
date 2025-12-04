
low = 0
ok = 0
high = 0

file = open("temperature.csv", "r")
lines = file.readlines()

for line in lines:
    line = line.strip()
    data = line.split(',')
    if data[2] == 'OK':
        ok += 1
    elif data[2] == 'LOW':
        low += 1
    else:
        high += 1

print(f"OK: {ok}")
print(f"LOW: {low}")
print(f"HIGH: {high}")