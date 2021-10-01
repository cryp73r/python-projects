from re import *
def check(t):
    mo = compile(r'\d{5} \d{5}')
    for i in mo.findall(t):
        print(i)

message = '''Hello! MY name is Priyanshu Singh. My Contact No is 93057 64393'''
check(message)
