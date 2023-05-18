import pywhatkit as pwt


def buscar_en_internet(texto):
    texto_sin_busca = texto.replace("busca", "").strip()
    pwt.search(texto_sin_busca)