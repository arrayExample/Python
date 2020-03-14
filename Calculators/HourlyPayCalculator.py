print("ABC Inc., Gross Pay Calculator!")
employee_name = str
while employee_name != 0:
    employee_name = str(input("Enter employee's name or 0 to quit: "))
    if employee_name == "0":
        print("Exiting program...")
        break
    hours_worked = int(input("Enter hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    if hours_worked > 40:
        over_time_time = hours_worked - 40
        over_time_pay = pay_rate * 1.5
        gross_pay_with_OT = (over_time_pay * over_time_time) + (40 * pay_rate)
        print("Employee Name: ", employee_name, "\nGross Pay: ", gross_pay_with_OT)
        print("(overtime pay: ", over_time_time * over_time_pay ,")")
    elif hours_worked <= 40:
        over_time_time = hours_worked - 40
        over_time_pay = pay_rate * 1.5
        gross_pay_no_OT = hours_worked * pay_rate
        print("Employee Name: ", employee_name, "\nGross Pay: ", gross_pay_no_OT)
""""
Test Value(s)
ABC Inc., Gross Pay Calculator!
Enter employee's name or 0 to quit: Nathan
Enter hours worked: 35
Enter employee's pay rate: 10.00
Employee Name: Nathan
Gross Pay: 350.0
Enter next employee's name or 0 to quit: Toby
Enter hours worked: 45
Enter employee's pay rate: 10
Employee Name: Toby
Gross Pay: 475.0
(overtime pay: 75.0 )
Enter next employee's name or 0 to quit: 0
Exiting program..."""