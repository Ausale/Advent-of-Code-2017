
checksum = 0

with open("spreadsheet.txt") as f:
    for line in f:
        list = [int(i) for i in line.split()]
        checksum += (max(list) - min(list))
print(checksum)
