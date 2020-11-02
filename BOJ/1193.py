X=int(input(""))
stage=0
while(X>stage):
    X-=stage
    stage+=1
if stage%2!=0:
    print("{0}/{1}".format(stage-X+1,X))
else:
    print("{1}/{0}".format(stage-X+1,X))