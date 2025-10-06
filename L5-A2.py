# finding hcf
# enter 2 numbers
numberLargest = int(input("enter the largest number: "))
numberSmallest = int(input("enter the smallest number: "))

# euclidean algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("hcf is: ", numberLargest)