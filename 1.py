# exercise 1:

Celsius = int(input("Enter Celsius degree: "))
print("Celsius is : {0} , Fahrenheit is : {1}".format(Celsius, (9.0/5.0)*Celsius+32.0))
print('-------------------------------------------------')

# exercise 2:

f = 1

for n in range(0, 21):
    print('{0}! = {1}'.format(n, f))
    n += 1
    f *= n
print('-------------------------------------------------')

# exercise 3:

for n in range(0, 10, 1):
    print('{0:<5d}{1:<5d}{2:<5d}'.format(n, n**2, n**3))
print('-------------------------------------------------')

# exercise 4:

number = int(input("Enter number :"))
div = int(input("enter second number: "))

while div != 0:
    temp = number % div
    number = div
    div = temp

print("The GCD of two numbers is : {0}".format(number))