n = int(input("Enter a number: "))

if n % 2 == 0:
    e = {n: [n ** 2, n ** 3]}
    print(e)
else:
    o = {n: [n ** 2, n ** 3]}
    print(o)
