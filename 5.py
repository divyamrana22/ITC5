Input_Rows = int(input("Enter number of rows "))
Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

x=0

for i in range(Input_Rows):
   
    row = ''
    for m in range(i+1):
        row += Alphabets[x%len(Alphabets)]

        x+=1
#when we enter an input such that x just exceeds 26, the remainder of 'x%len(Alphabets)' becomes 1 and the first index, i.e. 'A' repeates itself
    print(row)
