lst = []                                       # empty list

n = int(input("Enter number of elements : "))  # get the input value form the user

for i in range(0, n):
            a = int(input())
            lst.append(a) 
print("Input: list1 =",lst)
print("Output: Positive value in the list1 =")
for num in lst: 
      
    if num >= 0:                                  # check whether the number is greater than zero or not     
       print(num, end = " ,")                     # if it is grater than zero then print only the positive values

##output##
Enter number of elements : 5
12
-7
5
64
-14
Input: list1 = [12, -7, 5, 64, -14]
Output: Positive value in the list1 =
12 ,5 ,64 ,
