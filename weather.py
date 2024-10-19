import requests 


print ("------Welcome to Divyansh's Weather Checker!!------")


city_name = input("Enter your City : ")
API_key = "d2f43bb3876000160b1d0bf47f681ee0"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code==200 :
    data = response.json()
    print('Weather is' ,data ['weather'][0]['description'])
    print('Current temperature is ', data['main']['temp'])
    print('Current Temperature feels like ', data['main']['feels_like'])
    print('Humidity is ', data['main']['humidity'])
    print('Sea Level is ', data['main']['sea_level'])