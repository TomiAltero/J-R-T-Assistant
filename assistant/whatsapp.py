import pywhatkit as pwt

def mensaje_whatsapp(numero: str, mensaje: str, hora: int, minuto: int):
    try:
        pwt.sendwhatmsg(f"+{numero}", mensaje, hora, minuto)
        print("Datos recibidos correctamente. Mensaje en proceso")
    except Exception as e:
        print(f"Error al enviar el mensaje de WhatsApp: {str(e)}")
    except SyntaxError as err:
        print("Hay un error en la sintaxis")

