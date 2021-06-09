
checksum = 0

with open("spreadsheet.txt") as f:
    for line in f:
        list = [int(i) for i in line.split()]

        for value in list:
            for divisor in list:
                if value % divisor == 0 and value != divisor:
                    checksum += value // divisor
print(checksum)