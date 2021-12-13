#Write pseudo code:
#Create a variable to control the loop.
#Step-1: Ask user the purchase price of the house.
#Step-2: Ask the user the total cost of the house.
#Step-3: Ask the user the  percentage of down payment(x for x%).
#Step-4: Calculate the down payment.i.e down payment \
        #=( total cost)*(percentage of down payment/100)
##Step-5: Ask the user the amount of loan.i.e principal.
#Step-6: Ask the user the ceedit score.
#Step-7:Determine the Annual Percentage Rate.
#Step-8:Divide apr by 100.
#Step-9:Calculate monthly interest rate by dividing mon_int_rate by 12.
#Step-10:Ask the user number years of loan.
#Step-11:Calculate the number of monthly payments by multiplying years and 12.
#Step-12:Ask the user maximum monthly payment that the user can afford.
#Step-13:Calculate the monthly payment.
# Using the formula:
#monthly payment = po*r*((1+r)**n)/((1+r)**n-1).
#Step-13:Display all the results.

#Calculating monthly mortgage payments.

# Global constants:
APPLICATION_FEE = 250
APPRAISAL_FEE = 250
ATTORNEY_FEE = 2000
CREDIT_REPORT = 100
HOME_INSPECTION = 500
HOA_TRANSFER_FEE = 250

# Define main function.
def main():
    welcome_msg()
    #program_output()
    payment()

def welcome_msg():
    print()
    print('********************************************************')
    print('                 WELCOME HOME !                         ')
    print('*********************************************************')
    print()

#def program_output():
   # print('Total cost($)\tPrincipal($)\tDown payment($)\tMonthly interest rate($)\tYears\tMonthly payment($)')
   # print('---------------------------------------------------------------------')
   # print(total_cost,'\t',principal,'\t',down_payment,'\t',mon_int_rate,'\t',years,'\t',mon_payment)

def payment():

    # Create a variable to control the loop.
    again = 'y'

    while again == 'Y' or again == 'y':
    # Prompt the user:
    # The purchase price of the home you want to buy.
          purchase_price = int(input('Enter the purchase price of the home:'))
    # The total cost of house.
          total_cost = float(APPLICATION_FEE +APPRAISAL_FEE + ATTORNEY_FEE + CREDIT_REPORT + HOME_INSPECTION + HOA_TRANSFER_FEE+ purchase_price)
          print('The total cost of house : $',total_cost,sep='')
    #The down payment.
          down_payment = float(input('Enter the down payment (x for x%):'))
          down_payment = float(total_cost * (down_payment/100))
          print('The down payment is: $',format(down_payment,',.2f'),sep='')
    # The amount of the loan.
          principal = float(total_cost - down_payment)
          print('The amount of the loan :$',principal)
    # The credit score.
          credit_score = int(input('Enter the credit score earned:'))
          if credit_score > 720:
              ann_perc_int = 5.71
              print('The annual percentage interest rate is (x for x%):'+ \
                     str(ann_perc_int))
          elif credit_score >=620 or credit_score <= 720:
              ann_perc_int = 5.79
              print('The annual percentage interest rate is (x for x%):'+ \
                     str(ann_perc_int))
          else:
              ann_perc_int = 8.45
              print('The annual percentage interest rate is (x for x%):',+ \
                    str(ann_perc_int))
    
    # Divide apr by 100.00 and assign the result back to ann_perc_int.
          ann_perc_int = float(ann_perc_int / 100.00)
          
    # Monthly interest rate .
          mon_int_rate= float(ann_perc_int /12)
    # The number of years of the loan.
          years =float(input('Enter the number of years of the loan: '))
    # Number of monthly payments .
          num_mon_payment = float(years * 12)
    # The maximum monthly payment that the user can afford.
    # use a variable named 'max'.
          max = float(input('Enter the maximum that the user can afford: '))
    # Calculate the monthly payment that must be paid for this loan.
          a = float(principal * mon_int_rate * ((1 + mon_int_rate)**num_mon_payment))
          b = float((1 + mon_int_rate)**num_mon_payment)
          mon_payment = float(a/b)
          print('The monthly payment is $',format(mon_payment , ',.2f'),sep='')
          total_pay = str(mon_payment * num_mon_payment)   
          print('THe total amount you  will be paying is:', total_pay)
          print('The total amount you will be paying on the loan of ', principal ,'is ',total_pay ,'over',years,'years')
          if mon_payment <= max:
             print('yes ,you can afford this loan.')
          else:
              print('You cannot afford this loan.')
              
           
          again = input('Do you want to do loan calculation again?(y =yes):')     
     


main()





    

    








#Calculating monthly mortgage payments.
APPLICATION_FEE = 250
APPRAISAL_FEE = 250
ATTORNEY_FEE = 2000
CREDIT_REPORT = 100
HOME_INSPECTION = 500
HOA_TRANSFER_FEE = 250







# Define a function called payment.



def main():
    menu()
    payment()
    house_cost()



    
def menu():
    print('****************welcome to homeloan project*********************')
    print('----------------------------------------------------------------')
    print('CALCULATING THE MONTHLY PAYMENT')
    
    
    

    
def payment():
    global rate
    # Create a variable to control the loop.
    again = 'y'

    while again == 'Y' or again == 'y':
    # Prompt the user:
    # The purchase price of the house you want to buy.
          purchase_price = int(input('Enter the purchase price of the home:'))
    # The total cost of the house.
          total_cost = float(APPLICATION_FEE +APPRAISAL_FEE + ATTORNEY_FEE + CREDIT_REPORT + HOME_INSPECTION + HOA_TRANSFER_FEE+ purchase_price)
          print('The total cost of house : $',total_cost,sep='')
    #The down payment.
          down_payment = float(input('Enter the down payment (x for x%):'))
          down_payment = float(total_cost * (down_payment/100))
          print('The down payment is: $',down_payment)
    # The amount of the loan.
          principal = float(total_cost - down_payment)
          print('The amount of the loan :$',principal)
    # The credit score.
          credit_score = int(input('Enter the credit score earned:'))
          if credit_score > 720:
              ann_perc_int = 5.71
              print('The annual percentage interest rate is (x for x%):'+ \
                     str(ann_perc_int))
          elif credit_score <= 719 or credit_score >= 620:
              ann_perc_int = 5.79
              print('The annual percentage interest rate is (x for x%):'+ \
                     str(ann_perc_int))
          else:
              ann_perc_int = 8.45
              print('The annual percentage interest rate is (x for x%):',+ \
                    str(ann_perc_int))
    
    # Divide apr by 100.00 and assign the result back to ann_perc_int.
          ann_perc_int = float(ann_perc_int / 100.00)
          
    # Monthly interest rate .
          mon_int_rate= float(ann_perc_int /12)
    # The number of years of the loan.
          years =float(input('Enter the number of years of the loan: '))
    # Number of monthly payments .
          num_mon_payment = float(years * 12)
    # The maximum monthly payment that the user can afford.
    # use a variable named 'max'.
          max = float(input('Enter the maximum that the user can afford: '))
    # Calculate the monthly payment that must be paid for this loan.
          a = float(principal * mon_int_rate * ((1 + mon_int_rate)**num_mon_payment))
          b = float((1 + mon_int_rate)**num_mon_payment)
          mon_payment = float(a/b)
          print('The monthly payment is $',format(mon_payment , ',.2f'),sep='')
          total_pay = str(mon_payment * num_mon_payment)   
          print('THe total amount you  will be paying is:', total_pay)
          print('The total amount you will be paying on the loan of ', principal ,'is ',total_pay ,'over',years,'years')
          if mon_payment <= max:
             print('yes ,you can afford this loan.')
          else:
              print('You cannot afford this loan.')
              
           
          again = input('Do you want to do loan calculation again?(y =yes):')     
     


main()





    

    
