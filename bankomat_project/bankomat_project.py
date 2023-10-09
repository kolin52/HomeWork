
data = {'Kalin': 123, 'Ivan': 456 }
balance = {'Kalin': 500, 'Ivan': 4500 }

name = input('Enter your name: ')
if name in data.keys():
            print('Your name is accepted')
            
            print('Your balance is:', balance[name])
else:
            print('Wrong name')
            quit()
            
i = 1
while i < 4:
            pin_input = int(input('Enter pin:'))
            pin1 = int(data[name])
            

            if pin_input == pin1:
                        print('Pin code accepted')
                        i += 1
                        break
            else:
                        print('Wrong pin')
                        print('Your card is bloced')
                        quit()
                        
print('Login Successful')
print("Make a choice - 1 to 3 or exit")
print('1  Balance Inquiry')
print('2  Withdraw')
print('3  Deposit')


while True:
            
            try:
                        choice = int(input('Enter your choice:'))
                      
                        if choice == 1:
                                    print('Your balance is: ', balance[name])
                                    break
                        elif choice == 2:
                                    withdraw_sum = int(input('Please write withdraw sum: '))
                                    balance1 = balance[name] - withdraw_sum
                                    print('Your current balance is: ', balance1 )
                                    break
                        elif choice == 3:
                                    deposit_sum = int(input('Please write deposit_sum: '))
                                    balance2 = balance[name] + deposit_sum
                                    print('Your current balance is: ', balance2 )                                    
                                    break
                        
                        else:
                                    print('Wrong choice. Try again. Thank you for banking with us!')
                                    break
                                    
                                    
            except:
                        print('Wrong option. Try again')
                        
                        break