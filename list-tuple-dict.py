print("##################1#####################")
print("Assigning elemnts to differnt lists")
print("\n")
lst = []
n = int(input("enter the number of elements to the lst : "))
for i in range(0, n):
            a = int(input())
            lst.append(a)                      
print("Output: list =",lst)
print("\n")
print("##################2#####################")
print("Accessing elements from a tuple")
print("\n")
tupl = ('Apple','Banana','Cherry','Dates')
print("Print the second element in the tuples :",tupl[1])
tupl = tupl + ('Eggfruit',)
print("Add an element to the tuple :",tupl)
print("\n")
print("##################3#####################")
print("Deleting different dictionary elements")
print("\n")
dict = {"one" : 1, "two" : 2, "three" : 3, "four" : 4}
print("Before deleting an element :",dict)
del dict['three']
print("After deleting an element :",dict)

************************************************************************************************************************
OUTPUT

##################1#####################
Assigning elemnts to differnt lists


enter the number of elements to the lst : 5
1
2
3
4
5
Output: list = [1, 2, 3, 4, 5]


##################2#####################
Accessing elements from a tuple


Print the second element in the tuples : Banana
Add an element to the tuple : ('Apple', 'Banana', 'Cherry', 'Dates', 'Eggfruit')


##################3#####################
Deleting different dictionary elements


Before deleting an element : {'one': 1, 'two': 2, 'three': 3, 'four': 4}
After deleting an element : {'one': 1, 'two': 2, 'four': 4}
