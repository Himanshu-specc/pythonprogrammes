# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
m = n * 3
mod, dot, hyph = '|','.',  '-'
wel = 7 // 2 + 1
up = 1
low = n - 2
for i in range(1, n+1):
    if i == wel:
        print('Welcome'.center(m, hyph))

    while up < n and i < wel:
        print(str((dot + mod + dot) * up).center(m, '-'))
        up = up + 2
    while low > 0 and i > wel:
        print((str(dot+mod+dot) * low).center(m, '-'))
        low = low - 2




