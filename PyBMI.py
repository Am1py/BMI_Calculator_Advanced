print("!!!This calculator works with kilograms and meters!!!")
h = input("Enter your height: ")
w = input("Enter your weight: ")

def bmi_cal(w, h):
    try:
        h = float(h)
        w = float(w)
    except ValueError:
        print("Invalid values.")
    if w <= 0 or h <= 0:
        raise ValueError("Weight and height can't be negative numbers.")
    bmi=(float(w))/(float(h)**2)
    return (bmi)
bmi_cal(w, h)

bmi_result= bmi_cal(w, h)

if bmi_result > 0:
    def bmi_rate(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif  18.5 <= bmi < 25:
            return "Correct value"
        elif  25 <= bmi < 30:
            return "Overweight"
        else:
            return "1-st degree of obesity"
bmi_ratio=bmi_rate(bmi_result)

print(f"Your BMI  is equel to {bmi_result:.f}, it's {bmi_ratio}")



