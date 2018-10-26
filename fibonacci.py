c=0
x=0
y=1
fib=0
while c<100:
    c=c+1
    fib=x+y
    print(c,fib)
    x=y
    y=fib