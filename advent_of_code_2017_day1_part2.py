captcha = ""

sum = 0
index_two = 0

for index in range(len(captcha)):
    current_number = int(captcha[index])

    if int(index) >= int(len(captcha)//2):
        next_number = int(captcha[index_two])
        if current_number == next_number:
            sum += current_number
        index_two+=1

    else:
        next_number = int(captcha[index+(len(captcha)//2)])
        if current_number == next_number:
            sum += current_number

print(sum)
