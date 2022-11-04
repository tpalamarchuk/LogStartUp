import time
q1 = str(time.localtime())
a = q1
num_list = []

num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))

qrt1 = str(num_list[0]) + '-' + str(num_list[1]) + '-' + str(num_list[2]) + ' ~~~ ' + str(num_list[3]) + ':' + str(num_list[4])




with open("log.txt", "a", encoding = 'utf-8') as log:
    log.write("\nPC ON At:" + qrt1)
