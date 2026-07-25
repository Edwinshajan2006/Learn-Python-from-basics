def compare(a,b,c):
    if a>b and a>c:
        print (a)
    elif b>c and b>a:
        print(b)
    else :
        print (c)

a = input ("Enter first variable")
b = input("Enter the second number")
c = input("Enter the third number")
compare(a,b,c)