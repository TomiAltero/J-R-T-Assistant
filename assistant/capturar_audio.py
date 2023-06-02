import speech_recognition as spr

def obtener_audio():
    r = spr.Recognizer()
    with spr.Microphone() as mic:
        print("Habla ahora...")
        audio = r.listen(mic)
    return audio    

def reconocer_texto(audio):
    try:
        r = spr.Recognizer()
        print("Procesando audio...")
        texto = r.recognize_google(audio, language="es")
        print("Texto reconocido:", texto)
        return texto
    except spr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return None
