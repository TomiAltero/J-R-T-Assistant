import speech_recognition as spr
import pywhatkit as pwt
from buscar_google import buscar_en_internet
from reproduccion_yt import reproducir_youtube
from capturar_audio import obtener_audio, reconocer_texto
from obtener_clima import obtener_clima
from crear_alarma import establecer_alarma
from chistes import chistes
from whatsapp import mensaje_whatsapp


def main():
    while True:
        audio = obtener_audio()
        texto = reconocer_texto(audio)

        if texto is not None:
            if "Reproduce" in texto or "reproduce" in texto:
                reproducir_youtube(texto)
            elif "buscar" in texto or "busca" in texto:
                buscar_en_internet(texto)
            elif "clima" in texto:
                obtener_clima(texto)
            elif "alarma" in texto:
                establecer_alarma(texto)
            elif "Enviar mensaje" in texto:
                numero = input("Ingrese el numero: ")
                mensaje = input("Ingrese el mensaje: ")
                hora = int(input("Ingrese la hora que quieras mandar el mensaje: "))
                minuto = int(input("Ingrese el minuto que quieras mandar el mensaje"))
                mensaje_whatsapp(numero, mensaje, hora, minuto)

            elif "Cuéntame un chiste" in texto:
                chiste = chistes()
                print(chiste)
            else:
                print("No se reconoce el comando, vuelva a intentarlo")

            verif = input("Desea continuar (SI/NO): ")
            if verif == "NO":
                print("Nos vemos!")
                return

if __name__ == "main":
    main()