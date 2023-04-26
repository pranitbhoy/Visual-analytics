import  random
captcha=""
count =0
while count<6:
    list = ["@", "#", ]
    for i in range(48, 57, 1):
        list.append(chr(i))
    for j in range(65, 90, 1):
        list.append(chr(j))
    for i in range(48, 57, 1):
        list.append(chr(i))
    for k in range(97, 122, 1):
        list.append(chr(k))
    count=count+1
    value = random.choice(list)
    captcha=captcha+value


print(captcha)