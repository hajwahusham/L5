# to find the LCM

# input numbers
largest = int(input("enter the largest number: "))
smallest = int(input("enter the smallest number: "))

i = 1

while True:
    n = largest*i
    if n % smallest == 0:
        print("lcm = ", n)
        break
    i += 1

