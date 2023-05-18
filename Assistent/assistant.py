import speech_recognition as spr
import pywhatkit as pwt
from buscar_google import buscar_en_internet
from reproduccion_yt import reproducir_youtube
from capturar_audio import obtener_audio, reconocer_texto
from obtener_clima import obtener_clima
from crear_alarma import establecer_alarma


def main():
    audio = obtener_audio()
    texto = reconocer_texto(audio)

    if texto is not None:
        if "Reproduce" in texto or "reproduce" in texto:
            reproducir_youtube(texto)
        elif "busca" in texto or "Busca" in texto:
            buscar_en_internet(texto)
        elif "clima" in texto:
            obtener_clima(texto)
        elif "alarma" in texto:
            establecer_alarma(texto)



if __name__ == "__main__":
    main()