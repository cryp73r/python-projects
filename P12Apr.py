spam="qA2"
lis=[True, True, True, True, True]
spam=list(spam)
for i in range(0, len(spam)):
    if spam[i].isalnum()==True:
        lis[0]=True
        break
    else:
        lis[0]=False
for i in range(0, len(spam)):
    if spam[i].isalpha()==True:
        lis[1]=True
        break
    else:
        lis[1]=False
for i in range(0, len(spam)):
    if spam[i].isdecimal()==True:
        lis[2]=True
        break
    else:
        lis[2]=False
for i in range(0, len(spam)):
    if spam[i].islower()==True:
        lis[3]=True
        break
    else:
        lis[3]=False
for i in range(0, len(spam)):
    if spam[i].isupper()==True:
        lis[4]=True
        break
    else:
        lis[4]=False
for i in range(0, 5):
    print(lis[i])
