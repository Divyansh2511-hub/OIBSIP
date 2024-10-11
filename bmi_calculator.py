def category(bmi):
     if bmi < 18.5 :
          return "You are Underweight"
     elif 18.5 <= bmi < 24.9:
          return "You are Normally weighted"
     elif 25 <= bmi <= 29.9 :
          return "You are Overweight"
     else :
          return "You are Obese"
def main():
     print("Welcome to BMI Calculator")

weight = float(input("Enter your weight in kilograms :"))
height = float(input("Enter your height in meters :"))

if (weight <= 0 or height <= 0 ):
    print ("Invalid Values , try again !! ")

bmi = weight / ((height/100)**2)

classify = category(bmi)

print(f"Your Bmi is {bmi:.2f}")

print(f"Your Category is {classify}")