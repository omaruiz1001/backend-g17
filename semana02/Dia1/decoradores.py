def decoradorMayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@decoradorMayuscula
def mensaje(texto):
    return 'text : ' + texto

print(mensaje('hola mundo con decorador'))