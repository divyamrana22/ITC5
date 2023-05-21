1given_number = 5
initial = int(input("Enter intial range number  "))
final = int(input("Enter final range number "))

for i in range(initial,final,1):
   if i % given_number == 0:
      print(i)
