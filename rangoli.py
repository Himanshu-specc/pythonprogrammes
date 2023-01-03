l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
size = int(input('enter the size (size must be less than 26):  '))
ctr = size*4 - 3
for i in range(size*2):

    if i == size-1:
        print('-'.join(l[(size-1):0:-1] + l[0:size]))
    elif i < size:
        print('-'.join(l[size-1 : (size-1-i) : -1] + l[(size-1-i):size]). center(ctr, '-'))
    elif i > size:
        print('-'.join(l[(size - 1) : (i - (size)) : -1] + l[(i - size) : size] ).center(ctr, '-'))


