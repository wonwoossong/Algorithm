a=int(input())
first=1
i=6
square=1
# if a>=2 and a<=7:
#     print(2)
# elif a>=8 and a<=19:
#     print(3)
# elif a>=20 and a<=37:
#     print(4)
# elif a>=38 and a <=61:
#     print(5)
# else
#     print(6)
# 5받아
if a==1:
    print(square)
else:
    while(True):
        first+=i#7
        square+=1#2
        if a<=first:#true
            print(square)
            break
        i+=6
