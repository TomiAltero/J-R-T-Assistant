import requests
import json

def obtener_clima(ciudad):
    API_KEY = '5e9299c3f9207287280f06c6a59859c6'
    
    texto_limpio = ciudad.replace("clima" or "Clima", "")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={texto_limpio}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    vel_viento = data["wind"]["speed"]
    latitud = data["coord"]["lat"]
    longitud = data["coord"]["lon"]
    descripcion = data["weather"][0]["description"]
    pais = data["sys"]["country"]

    print(f"Temperatura: {temp}°C")
    print(f"Velocidad del viento: {vel_viento} m/s")
    print(f"Latitud: {latitud}")
    print(f"Longitud: {longitud}")
    print(f"Descripción: {descripcion}")
    print(f"País: {pais}")


