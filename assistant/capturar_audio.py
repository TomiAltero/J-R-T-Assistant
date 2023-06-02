import speech_recognition as spr

def obtener_audio():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print("Habla ahora...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
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