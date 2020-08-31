def divi(str):
    list=[]
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
    if list==['pop\n']:
        list.insert(0, 'pop')
    if list==['print\n']:
        list.insert(0, 'print')
    if list==['reverse\n']:
        list.insert(0, 'reverse')
    if list==['sort\n']:
        list.insert(0, 'sort')
    if len(list)==3:
        list[1]=int(list[1])
        list[2]=int(list[2])
    return list

li=[]
n=int(input())
for j in range(0, n):
    str=input()
    spam=divi(str)
    if spam[0]=='insert':
        li.insert(spam[1], spam[2])
    elif spam[0]=='remove':
        li.remove(int(spam[1]))
    elif spam[0]=='append':
        li.append(int(spam[1]))
    elif spam[0]=='sort':
        li.sort()
    elif spam[0]=='pop':
        li.pop()
    elif spam[0]=='reverse':
        li.reverse()
    elif spam[0]=='print':
        print(li)
