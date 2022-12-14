#The mother of all loops, the For loop
#The while loop keeps loopimh while its condition is True
#If you want to execute for a certain number of times, do this with a for loop and range()

#prints each letter in your name in a row
name=str(input("Please enter your name:"))
for i in name:
    print(i)

#prints each letter in your name in a column
name=str(input("Please enter your name:"))
for i in name:
    print(i,end="") #end parameter introduced
print()

#prints your name 5 times
#introducing the range() function
name=str(input("Please enter your name:"))
for i in range(5):
    print(f"{i}.{name}") #i indicates the number of times name is the variable

#increment for loop to find the sum of the first 100 numbers
count=0
for i in range(101):
    count+=i #
print(f"The sum of the first 100 numbers is {count}")

#more range methods
for i in range(12,16): #from 12 to 15
    print(i)

for i in range(0,100,10): #from 0 to 99 skipping 10 number intervals
    print(i)

for i in range(5,-1,-1) #counting down from 5 to 0 with a -1 interval
    print(i)

#end of for loop
