side_A = int(input("Enter side A "))
side_B = int(input("Enter side B "))
side_C = int(input("Enter side C "))

greatest_num = max(side_A,side_B,side_C)
smallest_num = min(side_A,side_B,side_C)
middle_num = (side_A+side_C+side_B) - (greatest_num + smallest_num)

if greatest_num < smallest_num + middle_num:
    S = (side_A + side_B + side_C)/2 
    A = ((S)*(S - side_A)*(S - side_B)*(S - side_C))**(1/2)

    print(f"Area of the given triangle is {A}")

else :
    print("The given sides do not belong to a triangle")