# Finger Exercise 2

# number = input("Insert your number here: ")
# number = int(number)

# if number > 0:
#     print("Your number is positive")
# elif number < 0:
#     print("Your number is negative")
# else:
#     print("Your number is zero")


# Problem Set 1 - A, B and C
"""
yearly_salary = 110000
portion_saved = .15
cost_dream_home = 750000

####### B
salary_raise = 0.03
#######  B
portion_down_payment = cost_dream_home * 0.25
annual_rate = 0.05

amount_saved = 0
months = 0

while amount_saved < portion_down_payment:
    

    amount_saved += (yearly_salary/12)  * portion_saved + amount_saved * (annual_rate/12)
    months += 1

    ####### B
    if months % 6 == 0:
        yearly_salary += yearly_salary * salary_raise
    ####### B

    # print(amount_saved, portion_down_payment,months)

print(f"It took you {months} months to get that amount saved.")


"""
# Problem Set 1 - C

annual_salary = 65000
portion_saved = .15
cost_dream_home = 750000
annual_rate = 0.05

####### B
salary_raise = 0.03
#######  B
portion_down_payment = cost_dream_home * 0.25
semi_annual_raise = 0.05

current_savings = 0 

steps_in_bisection_search = 0
low = 0
high = 10000

guess = int((low + high) / 2)
guessed_savings_rate = guess / 10000

def savings (current_savings , annual_salary , semi_annual_raise , guessed_savings_rate):
    
    for number_of_months in range(0 , 36):
        if number_of_months % 6 == 0 and number_of_months != 0:
            annual_salary += annual_salary * semi_annual_raise
            
        current_savings += guessed_savings_rate * annual_salary / 12 + current_savings * 0.04 / 12
                        
    return current_savings


current_savings = savings (0 , annual_salary , semi_annual_raise , high/10000)

if current_savings < portion_down_payment:
    print ("Unfortunately, it is not possible to pay for the down payment \
           in 36 months :(")
else:
    current_savings = savings (0 ,annual_salary , semi_annual_raise , guessed_savings_rate)
    steps_in_bisection_search += 1
    
    while abs(portion_down_payment - current_savings) >= 100:
        if  portion_down_payment > current_savings:
            low = guess
        else:
            high = guess
        guess = int((low + high) / 2)
        guessed_savings_rate = guess / 10000
        
        current_savings = int(savings (0 , annual_salary , semi_annual_raise , guessed_savings_rate))
        steps_in_bisection_search += 1

    print("Best savings rate:  " , guessed_savings_rate)
    print("Steps in bisecton search:  " , steps_in_bisection_search)