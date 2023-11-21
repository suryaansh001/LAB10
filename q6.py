def fac(n):
    
    
    if n==1 or n==0:
        return(1)
    else:
        return n* fac(n-1)
n=int(input("kripya number enter kijiye"))

print(fac(n))
    
