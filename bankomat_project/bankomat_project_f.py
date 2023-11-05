class Bankomat:
        
        def check_name_pin():
                data = {'Kalin': 123, 'Ivan': 456 }
                balance = {'Kalin': 500, 'Ivan': 4500 }
     
                name = input('Enter your name: ')
                
                try:
                        if name in data.keys():
                                print('Your name is accepted')
                        else:
                                print('Wrong name')
                                quit()

                        for i in range(3):       
                                        pin = int(input('Enter your pincode: '))                                     
                                        if pin == data[name]:
                                                print('Login Successful')
                                                print('Make a choice - 1 to 3 or exit\n 1  Balance Inquiry\n 2  Withdraw\n 3  Deposit')
                                
                                                choice = int(input('Enter your choice:'))
        
                                                if choice == 1:
                                                        print('Your balance is: ',balance[name] )
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
                               
                                                                print('Wrong option. Try again')  
                                                                break
                                        elif pin != data[name]:
                                                                print('Wrong pin code.')
                                                                i += 1  
                                        else:
                                                
                                            print('Pin code not accepted')
                                            quit()
     
                                        
                        
                except:
                        print('Wrong input')
                        quit()
            

        check_name_pin()