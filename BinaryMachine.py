'''
Binary Machine 10
Chra94

Converts binary to base 10 :)
'''
binary = '1000001'
n = -1
s = 0
for i in binary:
    n += 1
    if i == '1':
        if n != 0:
            s += 2**n
        else:
            s += 1

print(s)
