import csv
import pandas as pd
#create class in order to check correct user's name and pin
class Check_user_pin():

    def check_name():
        name = input('Write your name: ')
        users = pd.read_csv('/home/ka/users.csv')
        a = users.loc[:, 'user']
        if name in a:
            print('Your name is accepted')

    check_name()