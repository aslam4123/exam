def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    print(f)
a=int(input('enter the number:'))
fact(a)