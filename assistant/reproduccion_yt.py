import pywhatkit as pwt

def reproducir_youtube(texto):
    texto_sin_reproduce = texto.replace("Reproduce", "").strip()
    pwt.playonyt(texto_sin_reproduce)