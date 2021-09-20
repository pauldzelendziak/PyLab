while True:
    s = input ("Enter: (+,-,*,/) :")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input())
        y = float(input())
    if s == '+':
        print(x+y)
    if s == '-':
        print ('x-y')
    if s == '*':
        print(x*y)
    if s == '/':
        if y!=0:
            print (x/y)
        else:
            print ("Error")
