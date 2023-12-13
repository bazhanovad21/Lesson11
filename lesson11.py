
def vict():
    import random
    FAMOUS_PEOPLE = {'Пушкин': '26.06.1799', 'Лермонтов': '15.10.1814', 'Есенин': '03.10.1895',
     'Цой': '21.06.1962', 'Циолковский': '17.09.1857'}
    rounds = int(input('Сколько раз вы хотите сыграть?:'))
    for i in range (rounds):
    name ,date = random.choice(list(FAMOUS_PEOPLE.items()))
    answer = input(f'Когда родился? {name}')
    if answer == date:
        print('Верно')
    else:
        print('Неверно')
    print('Пока')

