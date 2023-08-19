weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m):"))

bmi = weight / height ** 2
bmi = round(bmi, 2)
if bmi < 18:
    print(f"You BMI is {bmi} and your underweight")
elif bmi <= 24.9:
    print(f"Your BMI is {bmi} and your normal")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi} and your Pre-obese")
else:
    print(f"Your BMI is {bmi} and your clinically Obese")