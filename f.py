#Q1
import math
def area_of_circle(r):
   a = r**2 * math.pi
   return a
print (area_of_circle(3))

#Q2
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

#Q3
def times_tables(n, t=1):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    times_tables(n, t+1)

times_tables(int(input("enter no:")))

#Q4
def power(num,i):
    if(i==1):
       return(num)
    else:
       return(num*power(num,i-1))
b=int(input("Enter number: "))
c=int(input("Enter index: "))
pow=power(b,c)
print("{} raised to {}: {}".format(b,c,pow))

#Q5
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
