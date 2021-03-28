W = float(input("Enter your weight in kg: "))
H = float(input("Enter your height in cm: "))

BMI = W / (H/100)**2

if BMI < 18.5:
    print("Your BMI is ", "%.2f" % BMI, " which means you are underweight")

elif BMI >= 18.5 and BMI < 25:
    print("Your BMI is ", "%.2f" % BMI, " which means it is normal")

elif BMI >= 25 and BMI < 30:
    print("Your BMI is ", "%.2f" % BMI, " which means you are overweight")

else:
    print("Your BMI is ", "%.2f" % BMI, " That means doctor consultation is required")