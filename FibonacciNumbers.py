i=int(input("Enter Positive Number of Terms: "))
t1=0
t2=1
print(t1,",",t2,",",end=" ")
for a in range(2,i):
    next = t1 + t2
    print(next, end=", ")
    t1 = t2
    t2 = next
