s=str(input(""))
s=s.upper()
t=[]
for i in set(s):
    t.append(s.count(i))
idx=[i for i,x in enumerate(t) if x==max(t)]
if len(idx)>1:
    print("?")
else:
    print(list(set(s))[t.index(max(t))])
