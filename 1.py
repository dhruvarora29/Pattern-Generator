                         #codeforwin star patterns
chat =True
while chat:
    pattern=int(input('''

===========================================================
Select the star pattern:

1.Hollow square star pattern
2.Hollow square with diagnol star pattern
3.Rhombus star pattern
4.Hollow rhombus star pattern
5.Mirrored rhombus star pattern
6.Hollow mirror rhombus star pattern
7.Hollow right triangle star pattern
8.Hollow mirror right triangle star pattern
9.Inverted right triangle star pattern
10.Hollow inverted right triangle star pattern
11.Hollow inverted mirror right triangle star pattern
12.Pyramid star pattern

Pattern number is:
'''))
    if pattern==1:
    #1.hollow square
        print('You chose Hollow square star pattern')
        a=int(input('enter no. of collumns: '))
        b=int(input('enter no. of rows: '))

        for i in range(1):
            print('*'*a)
            for j in range(b-2):
                print('*'*1+' '*(a-2) + '*'*1)
            print('*'*a)
    
    elif pattern==2:
#2.hollow square with diagnol
        print('You chose Hollow square with diagnol star pattern')
        a=int(input('enter no. of collumns: '))
        b=int(input('enter no. of rows: '))
        for i in range(1):
            print('*'*a)
            for j in  range(b):
                print('*'*(a//2) + ' ' + '*'*(a//2))
                print('*'*(a//2-1)+ ' ' +'*'*(a//2-1)+ ' '+'*'*(a//2-1))
            print('*'*a)
    elif pattern==3:
#3.rhombus
        print('You chose Rhombus star pattern') 
        rows=int(input('enter no. of rows: '))
        for i in range(rows):
            print(' '*(rows-i) + '*'*rows)

    elif pattern==4:
#4.hollow rhombus
        print('You chose Hollow rhombus star pattern')
        rows=int(input('enter no. of rows: '))
        coll=int(input('enter no. of stars: '))
        for i in range(1):
            print(' '*(rows) + '*'*coll)
            for j in range(rows-1):
                print(' '*(rows-j-1) + '*'*1 + ' '*(coll-2) + '*'*1)
            print('*'*coll)

    elif pattern==5:
#5.mirrored rhombus
        print('You chose Mirrored rhombus star pattern')
        rows=int(input('enter no. of rows: '))
        coll=int(input('enter no. of stars: '))
        for i in range(rows):
            print(' '*i + '*'*coll)

    elif pattern==6:
#6.hollow mirror rhombus
        print('You chose Hollow mirror rhombus star pattern')
        rows=int(input('enter the no. of rows: '))
        coll=int(input('enter the no. of stars: '))
        for i in range(1):
            print('*'*coll)
            for j in range(rows+1):
                print(' '*(j+1) + '*'*1 + ' '*(coll-2) + '*'*1)
            print(' '*(j+2) + '*'*coll)

    elif pattern==7:
#7. hollow right triangle
        print('You chose Hollow right triangle star pattern')
        row=int(input('enter no. of rows: '))
        for i in range(1):
            print('*')
            for j in range(row-2):
                print('*'*1 + ' '*(j) + '*'*1)
        print('*'*row)

    elif pattern==8:
#8.hollow mirror right triangle
        print('You chose Hollow mirror right triangle star pattern')
        row=int(input('enter the no. of rows: '))
        for i in range(1):
            print(' '*(row-1) +'*'*1)
            for j in range(row-2):
                print(' '*(row-2-j) + '*'*1 + ' '*(j) +'*'*1)
            print('*'*row)
        
    elif pattern==9:        
#9.inverted right triangle
        print('You chose Inverted right triangle star pattern')
        row=int(input('enter no. of rows: '))
        for i in range(row):
            print('*'*(row-i))

    elif pattern==10:
#10.hollow inverted right triangle
        print('You chose Hollow inverted right triangle star pattern')
        row=int(input('enter no. of rows: '))
        coll=int(input('enter no. of stars'))
        for i in  range(1):
            print('*'*row)
            for j in range(row-2):
                print('*'*1 + ' '*(row-j-3) + '*'*1)
            print('*')

    elif pattern==11:   
#11.hollow inverted mirror right triangle
        print('You chose Hollow inverted mirror right triangle star pattern')
        row=int(input('enter no. of rows: '))
        for i in range(1):
            print('*'*row)
            for j in range(row-2):
                print(' '*(j+1) + '*'*1 + ' '*(row-3-j) +'*'*1)
            print(' '*(row-1) + '*'*1)
    elif pattern ==12:
#12.pyramid star pattern
        print('You chose Pyramid star pattern')
        row=int(input('enter no. of rows: '))
        for i in range(row):
            print(' '*(row-i) + '*'*(2*i+1))

    else:
        print('Your option is not listed')
chat=False
