def goto(linenum): #This function helps us execute specific set of codes as and when required. To understand more, refer the 'jump_example.py" program in the same repository.
    """This function helps us execute specific set of codes as and when required."""
    global line
    line = linenum

line=0 #Initialize our variable
print("Please enter 10 decimal numbers:")

myarray=[]

i=0
while i<10: #While loop instead of for loop because our goto function does not work well with for loop.
    line=10 #This is the condition under which our desired code runs.
    try: #Try block.
        if line==10:
            myarray.append(float(input("Enter a number:"))) #This is our desired code. We are appending the entered number to the array.
        goto(20) #If this line executes, then the user entered a number as intended. If not, then this line will not be executed.
    except ValueError: #If we enter a value other than a number, we need to ask the user to enter a number again.
        print("You did not enter a number!!!") #Letting the user know that they did not enter a number.
        goto(10) #We execute the desired code again without incrementing i, so we do not skip the value of this index.
    if line==20: #If a user enters a number correctly, we need to prepare for getting next number.
        i=i+1 #Incrementing i.
    if i==10: #If the user enters 10 numbers correctly, the value of i will be 10 by now.
        print("Finished getting inputs.")

print("Entered array is:", myarray) #Print the current array.

for i in range(10): #This is the part where we swap the contents.
    if i%2==0: #If the index is even (0,2,4,6,8), then we swap. Else we continue.
        temp=myarray[i]
        myarray[i]=myarray[i+1]
        myarray[i+1]=temp
    else: #If we don't continue when the index is odd, then we will have an array with only the first value moved to the last position.
        #1,2,3,4,5,6,7,8,9,0 to 2,3,4,5,6,7,8,9,0,1
            #Also, we get index out of bounds exception, since we use i+1
        continue

print ("Swapped array is:", myarray) #Print the swapped array.