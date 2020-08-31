x = int(input())
y = int(input())
z = int(input())
n = int(input())
i=0
j=0
k=0
spam=[]
while i<=x:
    while j<=y:
        while k<=z:
            if (i+j+k)!=n:
                lis=[i, j, k]
                spam.append(lis)
            k=k+1
        j=j+1
    i=i+1
print(spam)
sp=[]
for i in range(0, len(spam)):
    if spam[i] not in sp:
        sp.append(spam[i])
s=[]
s=s.append(sp)
print(s)
