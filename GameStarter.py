from CityService import CityService

city_service = CityService()

print('Давай поиграем в города! (для выхода введи exit)')

user_city = input()
lastletter = None
while user_city != 'exit':
    if lastletter is None or user_city[0].lower() == lastletter:
        if city_service.is_city_exist(user_city):
            if not (city_service.is_used_city(user_city)):
                city_service.set_city_used(user_city)
                pc_city = city_service.get_city(user_city[-1])
                if pc_city is None:
                    print(f'Ты победил! Я не знаю города на букву {user_city[-1]}')
                    break
                else:
                    lastletter = pc_city[-1]
                    city_service.set_city_used(pc_city)
                    print(f'{pc_city} Твой ход. Введи город на букву {lastletter}..')
            else:
                print(f'Город {user_city} уже был назван. Введи другой город на букву {lastletter}..')
        else:
            print(f'Я не знаю города {user_city}. Введи другой город на букву {lastletter}..')

    user_city = input()
print('End!')
