# Задача 20. Да се напише програма, която да намира най-близкото 
#число палиндром дo  въведено цяло число от клавиатурата.
# Вход: 887
# Изход: 888
# Вход: 100
# Изход: 99
# Вход: 888
# Изход: 888
# Вход: 27
# Изход: 22

num = input('Enter digit: ')
if num == num[::-1]:
    print('It is palindrome')
elif num != num[::-1]:
    