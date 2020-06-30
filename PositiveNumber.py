lst = []                                            # empty list
lst1 = []                                              # empty list

# these following code is for the list 1

n = int(input("Enter number of elements for list1 : "))  # get the input value form the user

for i in range(0, n):
            a = int(input())
            lst.append(a)                       # adding the input values to the lst
print("Input: list1 =",lst)
print("Output: Positive value in the list1 = ")
for num in lst: 
      
    if num >= 0:                                 # check whether the number is greater than zero or not      
        print(num, end = " ,")  # if it is grater than zero then print only the positive values

print("\n")

# these following code is for the list 2
        
t = int(input("Enter number of elements for list2 : "))  # get the input value form the user

for c in range(0, t):
            b = int(input())
            lst1.append(b)                       # adding the input values to the lst
print("Input: list2 =",lst1)
print("Output: Positive value in the list2 = ")
for num1 in lst1: 
      
    if num1 >= 0:                                 # check whether the number is greater than zero or not      
        print(num1, end = " ,")  # if it is grater than zero then print only the positive values

**********************************************************************************************************************************************************
OUTPUT

Enter number of elements for list1 : 5
12
-7
5
64
-14
Input: list1 = [12, -7, 5, 64, -14]
Output: Positive value in the list1 = 
12 ,5 ,64 ,

Enter number of elements for list2 : 4
12
14
-95
3
Input: list2 = [12, 14, -95, 3]
Output: Positive value in the list2 = 
12 ,14 ,3 ,

