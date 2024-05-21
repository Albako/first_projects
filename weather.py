import requests


class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

      

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=cb2d6d0a84b98ebc3341043490a1df2a")

            

        except:
            print("No internet access :(")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp}°{units_symbol}")
        print(f"Today's High: {self.temp_max}°{units_symbol}")
        print(f"Today's Low: {self.temp_min}°{units_symbol}")



vacation_city = City("Cairo", 30.033333, 31.233334)
vacation_city.temp_print()

vacationF_city = City("Cairo", 30.033333, 31.233334, units = "imperial")
vacationF_city.temp_print()

my_city = City("Wroclaw", 51.107883, 17.038538) 
my_city.temp_print()

myF_city = City("Wroclaw", 51.107883, 17.038538, units = "imperial") 
myF_city.temp_print()

norwegianCapital_city = City("Oslo", 59.911491, 10.757933)
norwegianCapital_city.temp_print()

norwegianCapitalF_city = City("Oslo", 59.911491, 10.757933, units = "imperial")
norwegianCapitalF_city.temp_print()

casino_city = City("Las Vegas", 36.188110, -115.176468)
casino_city.temp_print()

casinoF_city = City("Las Vegas", 36.188110, -115.176468, units = "imperial")
casinoF_city.temp_print()