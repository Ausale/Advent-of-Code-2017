captcha = ""

sum = 0

for index in range(len(captcha)):
    current_number = int(captcha[index])

    if index == len(captcha)-1:
        if current_number == int(captcha[0]):
            sum += current_number
    else:
        next_number = int(captcha[index+1])
        if current_number == next_number:
            sum += current_number

print(sum)

