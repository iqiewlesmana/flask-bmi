#check BMI
weight=input('Please enter your wt in kg : ')
height_in_cm=input('Please enter your height in cm :eg 172 as 5.9 : ')
#feet and inches to meter
height_in_m=float(height_in_cm/100)
#calculate BMI
bmi=float(weight)/float(height_in_m**2)

if bmi  <=18.5:
    print('You are Under weight as your bmi is {}'.format(bmi))
elif (bmi >=18.5) and (bmi <=24.9):
     print('Perfect!You have normal weight and your bmi is {}'.format(bmi))
elif (bmi >=25) and (bmi <=29.9):
     print('You are Overweight as your bmi is {}'.format(bmi))
elif bmi>=30:
     print('You are highly obese as your bmi is {}'.format(bmi))
else :
     print('Renter properly')