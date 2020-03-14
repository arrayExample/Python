student_name = str
print('Welcome to the BMI Index Calculator.')
while student_name != 0:
    student_name = str(input('Please begin by entering the student\'s name, or 0 to quit: '))
    if student_name == "0":
        print("Exiting program...")
        break
    else:
        def height():
            student_height = int(input('Please enter student\'s height in inches: '))
            return student_height
        sheight = height()

        def weight():
            student_weight = int(input('Please enter student\'s weight in pounds: '))
            return student_weight
        sweight = weight()

        def bmi_calc():
            bmi = (sweight * 703) / (sheight ** 2)
            return bmi
        bmicalc = bmi_calc()

        def bmi_output():
            print (student_name, "\'s BMI profile:\n-----------------------")
            print ("Height: ", sheight, "\nWeight: ", sweight, "\nBMI Index: ", round(bmicalc, 1))

        bmi_calc()
        bmi_output()
"""Test Variables/Output
Welcome to the BMI Index Calculator.
Please begin by entering the student's name, or 0 to quit: Nathan
Please enter student's height in inches: 70
Please enter student's weight in pounds: 135
Nathan 's BMI profile:
-----------------------
Height: 70"
Weight: 135 lbs.
BMI Index: 19.4
Enter next student's name or 0 to quit: Toby
Please enter student's height in inches: 73
Please enter student's weight in pounds: 310
Toby 's BMI profile:
-----------------------
Height: 73"
Weight: 310 lbs.
BMI Index: 40.9
Enter next student's name or 0 to quit: 0
Exiting program..."""