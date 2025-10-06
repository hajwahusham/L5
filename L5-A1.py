# check if a number is a palindrome or not

# input from user
number = int(input("enter your number: "))

# store the original number for comparision
original_number = number
reversed_number = 0
# reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
# check if the original number & reverse number are the same
if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")