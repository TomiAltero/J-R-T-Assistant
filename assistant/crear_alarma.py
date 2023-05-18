import datetime
from playsound import playsound

def reproducir_sonido(nombre_archivo):
    playsound(nombre_archivo)


def sonar_alarma(alarma):
    while True:
        horario = datetime.datetime.now().strftime("%H:%M")
        if horario == alarma:
            print("ALARMA SONANDO!")
            reproducir_sonido("alarma.mp3")
            break


def establecer_alarma(voz):
    
    if "alarma" in voz:
        voz_limpio = voz.replace("alarma" or "Alarma", "").strip()
        sonar_alarma(voz_limpio)

