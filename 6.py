#making a list of enteries
input_range = input('Enter range values seperated by a comma(no spaces): ').split(',')
List = list(input_range)

#defining range variables
m=int(List[0])
n=int(List[1])

    
for i in range (m+1,n):
    count = 0

    
    for x in range(1,i+1):
        if i%x == 0:
            count = count + 1
    if count <= 2 : 
        print(i)
        




