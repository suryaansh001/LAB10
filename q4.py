a,b=map(int,input("enter two numbers").split())
o=str(input("enter operation:+,-,*,/,^"))
if o=="+" or o=="add":
    print(a+b)
elif o=="-" or o=="subtract":
    print(a-b)
elif o=="*" or o=="multiply":
    print(a*b)
elif o=="^" or o="exponential":
    print(a**b)
elif o=="/" or o=="divide":
    try:
        print(a/b)
    except ZeroDivisionError:
        print("b cannot be 0")