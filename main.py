# firstly enter the number of legos
n = int(input())

# fesired range checked
if(n<1 or n > pow(10,5)):
    while(n<1 or n > pow(10,5)):
        print("You entered a value out of range. Please enter a integer number between 1 and 10^5")
        n = int(input())

# array created
arr = []

# in the same line our list is created
y = input()
arr= y.split(" ")[:n]


def findMinNumber(arr):

    # it is checked whether the elements of the array are in the desired range.
    while any(int(i) < 1 or int(i) > pow(10, 5) or len(arr) != n for i in arr):
        arr= []
        print("You entered a value out of range or missing number.\n" 
              "Please enter integer numbers between 1 and 10^5 and and leave a space between the numbers")
        y = input()
        arr = y.split(" ")[:n]

# first loop tries to find the min number by starting from 1 and increasing by one.
    for j in range(1, pow(10,5)):

        # in each cycle, the energy is equalized to new number
        ballEnergy = j

        # second loop calculates the minimum number tried, the delta, and tries it in all the array elements.
        for k in range(n):
            delta = ballEnergy - int(arr[k])
            ballEnergy = delta + ballEnergy

# if the energy is still greater than 0 when the last element is reached. The minimum number is equal to j
        if (ballEnergy >= 0):
            break
    print(j)

findMinNumber(arr)

