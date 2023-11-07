import csv
import pandas as pd
#create class in order to check correct user's name and pin
class Check_user_pin():
#Function to check correct name
    def check_name():
        name = input('Write your name: ')
        users = pd.read_csv('/home/ka/users.csv')
        a = users.loc[:, 'user']
        if name in a:
            print('Your name is accepted')
#Function to check correct pincode            
    def check_pin():
            try:
                for i in range(3):
                                        pin = int(input('Write your pin: '))
                                        pincode = pd.read_csv('/home/ka/users.csv')
                                        p = pincode['pincode']
                                        if pin in p:
                                                print('Login Successful')
                                                print('Make a choice - 1 to 3 or exit\n 1  Balance Inquiry\n 2  Withdraw\n 3  Deposit')
                                
                                                choice = int(input('Enter your choice:'))
        
                                                if choice == 1:
                                                        balance = pd.read_csv('/home/ka/users.csv')
                                                        b = balance['balance']
                                                        

                                                        print('Your balance is: ',b[0] )
                                                        break
                                                elif choice == 2:
                                                                withdraw_sum = int(input('Please write withdraw sum: '))
                                                                balance1 = b[0] - withdraw_sum
                                                                print('Your current balance is: ', balance1 )
                                                                break
                                                elif choice == 3:
                                                                deposit_sum = int(input('Please write deposit_sum: '))
                                                                balance2 = b[0] + deposit_sum
                                                                print('Your current balance is: ', balance2 )                                    
                                                                break
                                                
                                                else:
                                                                print('Wrong choice. Try again. Thank you for banking with us!')
                                                                break                 
                               
                                                                print('Wrong option. Try again')  
                                                                break
                                        elif pin != p[0]:
                                                                print('Wrong pin code.')
                                                                i += 1  
                                        else:
                                                
                                            print('Pin code not accepted')
                                            quit()           
            except:
                        print('Wrong input')
                        quit()
            

    check_name()
    check_pin() 
