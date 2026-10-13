n=int(input(5))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
     print()   