class Employee:
  
    def __init__(self):
        self.emp_name = ""
        self.emp_rate = 7.25
        self.emp_regular = 0.0
        self.emp_overtime = 0.0
        self.hours_worked = 0.0

    
    def set_name(self, emp_name):
        self.emp_name = emp_name


    def get_name(self):
        return self.emp_name


    def set_rate(self, emp_rate):
        self.emp_rate = emp_rate

   
    def get_rate(self):
        return self.emp_rate

  
    def set_hours_worked(self, hoursWorked):
        if hoursWorked > 40.0:
            self.emp_regular += 40.0
            self.emp_overtime += hoursWorked - 40.0
        else:
            self.emp_regular += hoursWorked
        self.hours_worked += hoursWorked

   
    def get_hours_worked(self):
        return self.emp_regular + self.emp_overtime

   
    def get_regular_pay(self):
        regular_pay = self.emp_rate * self.emp_regular
        return regular_pay

  
    def get_overtime_pay(self):
        overtime_pay = 1.5 * self.emp_rate * self.emp_overtime
        return overtime_pay

    
    def get_gross_pay(self):
        return self.get_regular_pay() + self.get_overtime_pay()

   
    def get_tax(self):
        gross_pay = self.get_gross_pay()
        tax_percentage = 0
        if gross_pay >= 0 and gross_pay <= 2000.0:
            tax_percentage = 10
        elif gross_pay >= 2000.0 and gross_pay <= 3500.0:
            tax_percentage = 15
        elif gross_pay >= 3500.0 and gross_pay <= 6000.0:
            tax_percentage = 28
        elif gross_pay >= 6000.0 and gross_pay <= 10000.0:
            tax_percentage = 31
        elif gross_pay > 10000.0:
            tax_percentage = 36
        return tax_percentage


    def get_net_pay(self):
        gross_pay = self.get_gross_pay()
        return gross_pay - (gross_pay * self.get_tax()) / 100

    
    def __str__(self):
        return "Employee Name : {}\nTotal regular hours worked : {}\nTotal overtime hours worked : {}\nTotal hours worked : {}\nPay rate : ${}\nMonthly Regular Pay : ${}\nMonthly overtime pay : ${}\nMonthly gross pay : ${}\nMonthly taxes : {}%\nMonthly net pay : ${:.2f}\n".format(self.get_name(), self.emp_regular,self.emp_overtime,self.get_hours_worked(),self.get_rate(),self.get_regular_pay(),self.get_overtime_pay(),self.get_gross_pay(),self.get_tax(),self.get_net_pay())


def test(name, rate, hours_worked_list):
    emp = Employee()
    emp.set_name(name)
    emp.set_rate(rate)
    emp.set_hours_worked(hours_worked_list)

    print(emp.__str__())


if __name__ == "__main__":
    test("Jane Doe", 35.10, [40, 30, 40, 35])
    test("John Doe", 37.20, [40, 40, 40, 40])
    test("Chance Wylie", 65.50, [50, 35, 40, 55])


