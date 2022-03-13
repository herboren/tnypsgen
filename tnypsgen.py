import random
length = input("Length: ")
for l in range(10):
    dup = tmp = ''
    for i in range(int(length)):
        dup = chr(random.randint(33,127))
        if dup not in tmp:
            tmp += dup
    print(tmp)