#8. Да се състави програма, която да отгатне колко е студено/топло по
#въведената температура в градус Целзий. Температурните интервали са: 
#t <=-20 ледено студено; t <=0 && t>-20 студено; t <=15 && t>0 хладно; t <=25 && t>15 топло; t >25 горещо
#Входни данни: t - цяло число от интервала [-100..100].

temp = int(input('Въведете температурата на въздуха: '))

if temp <=-20:
    print('Времето е ледено студено')
elif temp <= 0 and temp > -20:
    print('Времето е студено')
elif temp > 0 and temp <= 15:
    print('Времето е хладно')
elif temp > 15 and temp <= 25:
    print('Времето е топло')
else:
    print('Времето е горещо')