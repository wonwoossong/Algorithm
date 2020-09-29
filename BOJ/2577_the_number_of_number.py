a=int(input(""))
b=int(input(""))
c=int(input(""))
total=list(str(a*b*c))
for i in range(10):
    print(total.count(str(i)))
#str convert value to string so we can compare them 
#for instance, we made the total value to string in list and i changed the value "i" to string for comparing each other 