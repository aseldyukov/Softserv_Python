import pyowm

#обєкт модуля pyowm
owm = pyowm.OWM('af7b989b0cac5102b6e383221a841f55')  

# You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
#метод weather_at_place від імені інстансу owm 
#отримує інформацію в певному місті 
city = input("Input city:")

observation = owm.weather_at_place(city)
#з змінної observation з допомогою 
#методу get_weather() отримуємо погоду
w = observation.get_weather()

t_min = w.get_temperature('celsius')['temp_min']
t_max = w.get_temperature('celsius')['temp_max']
t_avr = w.get_temperature('celsius')['temp']

print('In city:',city, 'temperature min: ', t_min, " for the Celsius")
print('In city:',city, 'temperature min: ', t_avr, " for the Celsius")
print('In city:',city, 'temperature min: ', t_max, " for the Celsius")

wind = w.get_wind()
for key in wind:
    print(key, 'of wind is:', wind[key])

humidity =  w.get_humidity()
print('humidity is:', humidity)


# print(w)                     # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)