import pyjokes

def chistes():

    chiste = pyjokes.get_joke(language='es', category= 'neutral')
    return chiste