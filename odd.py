# Coded by TheSpaceCowboy
# Github: https://www.github.com/TheSpaceCowboy42534
# Date: 29/12/17
def findOdd(num :int):
    numbers = [1] # Stores the numbers and starts from 1
    while True: # Itterates through every number up until num
        if(numbers[-1]+2 <= num): # Adding 2 to the output of the algorithm will always equal an odd number
            numbers.append(numbers[-1]+2) # Appends the number to the array 
        else:
            return numbers # Returns the array of odd numbers
        

