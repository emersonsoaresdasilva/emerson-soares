#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 09 |
#        Polimorfismo (Trybe)
#-------------------------------------

class Mamifero:
    def emitir_som(self):
        pass

class Cachorro(Mamifero):
    def emitir_som(self):
        print('Au... Au!')

class Gato(Mamifero):
    def emitir_som(self):
        print('Miau... Miau!')

class Rato(Mamifero):
    def emitir_som(self):
        print('Algum som que o rato faz.')

cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

for mamifero in mamiferos:
    mamifero.emitir_som()
