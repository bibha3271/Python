f=1
a=int(input("Enter a Number"))
if a<0:
    print("factorial cannot be found")
elif a==0:
    print(" Factorial of a is 1")   
else:
    for i in range(1,a+1):
        f=f*i
        print("the factorial of a number is", f)

