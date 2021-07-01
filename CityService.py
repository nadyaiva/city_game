class CityService:
    def __init__(self):
        self.__load_cities()

    def __load_cities(self):
        self.__allcities = {'c': ['Самара', 'Саратов'],
                            'у': ['Ульяновск'],
                            'к': ['Курск', 'Киров'],
                            'м': ['Москва'],
                            'т': ['Тула'],
                            'а': ['Архангельск'],
                            'в': ['Владимир'],
                            'р': []
                            }
        self.__usedcities = []

    def is_city_exist(self, city):
        first_letter = str(city)[0].lower()
        if first_letter in self.__allcities:
            return city in self.__allcities[first_letter]
        else:
            return False

    def is_used_city(self, city):
        return city in self.__usedcities

    def set_city_used(self, city):
        self.__usedcities.append(city)

    def get_city(self, letter):
        cities = self.__allcities[letter]
        for city in cities:
            if not self.is_used_city(city):
                self.set_city_used(city)
                return city
