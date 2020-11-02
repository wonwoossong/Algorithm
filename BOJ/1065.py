a=int(input(""))#단지 어디까지인지만 입력 받는거
hansu=0
for i in range(1,a+1):
    if i <=99:
        hansu+=1
    else:
        nums=list(map(int,str(i)))
        if nums[0]-nums[1] == nums[1] - nums[2]:
            hansu+=1
print(hansu)
    