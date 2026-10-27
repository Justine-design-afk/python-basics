#bmi table
# • Underweight: Below 18.5
# • Healthy Weight: 18.5 to 24.9
# • Overweight: 25.0 to 29.9
# • Obesity (Class I): 30.0 to 34.9
# • Obesity (Class II): 35.0 to 39.9
# • Severe Obesity (Class III): 40.0 or higher

weight=input("please enter your weight in kilos:")
height=input("please enter your height in metres:")

w=float(weight)
h=float(height)

bmi=w/(h*h)  #h**2, marh.pow(h,2)
# age==19
if bmi<18.5:
    print("you are underweight")
elif 18.5 <= bmi <= 24.9:
        print("you are healthy")
elif 25 <= bmi <= 29.9:
    print("you are obese")
elif 30 <= bmi <= 34.9:
    print("obese class 1")
elif 35<=bmi<=39.9:
    print("obese class 2")
else:
    print("obese class 3")




