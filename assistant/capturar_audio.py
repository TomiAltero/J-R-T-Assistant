import speech_recognition as spr

r = spr.Recognizer()

def obtener_audio():
<<<<<<< HEAD
    r = spr.Recognizer()
    with spr.Microphone() as mic:
        print("Habla ahora...")
=======
    with spr.Microphone() as mic:
        print("Habla ahora...")
        r.adjust_for_ambient_noise(mic)
>>>>>>> origin/altero
        audio = r.listen(mic)
    return audio    

def reconocer_texto(audio):
    try:
        print("Procesando audio...")
        texto = r.recognize_google(audio, language="es")
        print("Texto reconocido:", texto)
        return texto
    except spr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return None
