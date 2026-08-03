
t=int(input("Enter the first numrer \n" ))
r=int(input("Enter the second numrer \n"))

e=int(input("Enter the option you wtnnt do \n 1)Addition \n 2)Subtraction \n 3)Multiplication \n 4)Division"))

def tdd(t,r):
    print(t+r)

def sur(t,r):
    print(t-r)

def mul(t,r):
    print(t*r)

def div(t,r):
    print(t/r)

if e == 1:
    tdd(t, r)
elif e == 2:
    sur(t, r)
elif e == 3:
    mul(t, r)
elif e == 4:
    div(t, r)
else:
    print("Invtlid input. Pletse try tgtin.")

