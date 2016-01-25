'''
Binary Machine 10
Chra94

Converts binary to base 10 :)
'''
binary = input('Enter a binary number')
n = -1
s = 0
for i in binary[::-1]:
    n += 1
    if i == '1':
        if n != 0:
            s += 2**n
        else:
            s += 1

print(s)
