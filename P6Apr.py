list=[]
str=input()
str=str+'\n'
s=''
i=0
while i<len(str):
    if str[i]!=' ':
        s=s+str[i]
    if str[i]==' ' or str[i]=='\n':
        list.append(s)
        s=''
    i=i+1
list[0]=int(list[0])
list[1]=int(list[1])
list[2]=int(list[2])
print(list[::-1])
