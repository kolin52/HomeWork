#3. Трябва да се напълни цистерна с вода. Имате 2 кофи с вместимост 2 и 3 литра и ги ползвате едновременно.
#Да се състави програма, която по въведен обем извежда как ще прелеете течността с тези кофи, т.е.
#по-колко пъти ще се пълни всяка от кофите.
#Входни данни: естествено число от интервала [10..9999].

try:
    obem = int(input('Write digit between 10 and 9999: '))
    k1 = 2
    k2 = 3
    obem_kofi = k1 + k2
    ob_broi = obem//obem_kofi
    ostatak = obem%obem_kofi

    if obem%obem_kofi != 0 and ostatak%k1 == 0 and ostatak//k1 == 1:
        print('Each bucket will be full ', ob_broi, 'times and additional one bucket', k1)
    elif obem%obem_kofi != 0 and ostatak%k1 == 0 and ostatak//k1 == 2:
            print('Each bucket will be full ', ob_broi, 'times and additional two buckets 2 l - ', 2*k1, 'liters')
    elif obem%obem_kofi != 0 and ostatak%k2 == 0 and ostatak//k2 == 1:
            print('Each bucket will be full ', ob_broi, 'times and additional one bucket', k2)
    elif obem%obem_kofi == 0:
        print('Each bucket will be full ', ob_broi, 'times' )
    else:
        print('Each bucket will be full ', ob_broi, 'times and remainder is 1 l')


except:
    print('Enter correct digit')
