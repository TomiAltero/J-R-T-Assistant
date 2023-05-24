import requests


def chistes():
    response = requests.get('https://v2.jokeapi.dev/joke/Any', params={'lang': 'es'})

    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            joke = data['joke']
            print(joke)
        elif data['type'] == 'twopart':
            setup = data['setup']
            delivery = data['delivery']
            print(setup)
            print(delivery)
        else:
            print('No se encontraron chistes en español.')
    else:
        print('No se pudo obtener el chiste. Código de respuesta:', response.status_code)
