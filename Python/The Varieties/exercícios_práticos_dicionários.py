'''
Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.
lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário
pode ter as posições que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "fabio" e "maria".

(oficialmente, um dicionário não tem "posições",
mas sim chaves)
'''
agenda_exemplo = {}
agenda_exemplo['marcos']=32112232
agenda_exemplo['fabio']=988887788
agenda_exemplo['maria']=44554455 

'''
Rode o codigo no IDLE apertando F5

Se você digitar agenda_exemplo['maria'],
deverá ver o telefone da maria
'''

'''
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa
'''

# Exemplo: dicionario = {"Emerson": "11977506620"}
#                         Chave         Valor
# Retorna: 11977506620
def consulta(agenda, pessoa):
  return agenda[pessoa] # Retorna o telefone dessa pessoa.

'''
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples
dicionario['chave'] = valor
'''

# Exemplo: dicionario = {           :            }
#                         Chave         Valor
#   ''   : dicionario = {"Emerson": "11977506620"}

def adiciona(agenda,pessoa,telefone):
  agenda[pessoa] = telefone # Adiciona o telefone dessa pessoa na agenda.
  return 'adicionei'

'''
Rode o codigo no IDLE apertando F5

Ai, você pode testar sua função adiciona manualmente e também 
fazer o runTests
'''

'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe,
o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario 
    isso é um teste que retorna True se a chave
    está no dicionário, e False caso contrário.

Temos, por exemplo, os prints seguintes,
que verificam se algumas pessoas estao na agenda
'''
#print('maria esta na agenda?')
#print('maria' in agenda_exemplo)

#print('damiao esta na agenda?')
#print('damiao' in agenda_exemplo)

#pessoa = 'marcos'
#print('a string da variavel pessoa é uma chave da agenda?')
#print(pessoa in agenda_exemplo)

'''
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
'''

def verifica(agenda,pessoa):
  '''
  if pessoa not in agenda:
    return False
  return True
  '''
  return pessoa in agenda # True or False (direto).

''' 
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}

'''
Usando seus conhecimentos de dicionário até agora, 
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}

NAO USE nenhuma função mágica do python. Escreva a lógica
usando dicionários.

O seguinte trecho de codigo pode ser util:
>>> palavra='ganancia'
>>> nro_a = 0
>>> for letra in palavra:
	print('estou olhando para',letra)
	if letra == 'a':
		nro_a = nro_a+1
		
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a
nro_a = 3
'''

def conta_letras(palavra):
    contagem = {}
    # Para cada letra "chave no dicionário"... na palavra.
    for letra in palavra:
      # Se a letra "chave" não estiver na contagem...
      if letra not in contagem:
        contagem[letra] = 1   # {"letra": "1"} - A letra ocorreu somente 01 vez.
      else:
        contagem[letra] += 1  # {"letra": "2...n"} - A letra ocorreu mais de 01 vez.
    return contagem

'''
Agora, vamos usar listas e dicionários para criar uma agenda 
um pouco mais completa. Veja o exemplo
'''

agenda_melhor1 = {
        'lucas': {
            'email': 'lucas.goncalves@faculdadeimpacta.com.br',
            'telefones': [11999888999, 1177788899]
            }, #meu email está correto, meus telefones nao :P
        'maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
            },
        'marta': {
            'telefones':[1177788899]     
            }
        }

'''
Crie uma função email, que recebe uma agenda (dessas melhoradas)
e uma pessoa.

Ela retorna o email da pessoa. 

Não precisa se preocupar com
o caso do registro da pessoa nao ter email (faremos isso
mais pra frente)
'''
# Exemplo: agenda = {"Emerson": {"email": emersonsoares2001@gmail.com"}}
# Retorna: emersonsoares2001@gmail.com
def email(agenda,pessoa):
    return agenda[pessoa]["email"] # Acessando valor da chave "email".

'''
Crie uma função telefone_principal, que recebe uma agenda 
(nessa versão mais nova) e uma pessoa.

Ela retorna o primeiro telefone da lista de telefones da 
pessoa
'''
# Exemplo: agenda = {"Emerson": {"telefones": ["11977506620", "1100001234"]}}
# Retorna: 11977506620
def telefone_principal(agenda,pessoa):
    return agenda[pessoa]["telefones"][0]

'''
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir
>>> for chave in agenda_melhor1:
	print(chave)
lucas
maria
marta

Lembrando de qual a cara da agenda_melhor1:

{'marta': {'telefones': [1177788899]},
 'lucas': {'email': 'lucas.goncalves@faculdadeimpacta.com.br',
                       'telefones': [11999888999, 1177788899]},
 'maria': {'email': 'maria.aparecida@exemplo.com', 'telefones': [84999777444]}}

(ela realmente só tem essas 3 chaves)
'''
'''
Crie uma função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem email.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['marta']
'''

def sem_email(agenda):
    contatos_sem_emails = []
    for nome in agenda:                   # Para cada nome "chave" na agenda...
      if "email" not in agenda[nome]:     # Se não conter "email"...
        contatos_sem_emails.append(nome)  # Adiciona na lista.
    return contatos_sem_emails

'''
Crie uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!), 
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item marta
e no item lucas
'''

#agenda_telefones = {
#     'marta': {'telefones': [1177788899]},
#     'lucas': {'email': 'lucas.goncalves@faculdadeimpacta.com.br', 'telefones': [11999888999, 1177788899]}


def conta_telefones(agenda):
  telefones = 0
  for nome in agenda: # Para cada nome "chave" na agenda...
    telefones += len(agenda[nome]["telefones"]) # Faz a leitura dos telefones de cada pessoa... e soma a quantidade de telefones.
  return telefones

'''
Por ultimo, vamos criar uma funcao conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, as vezes que cada 
número apareceu na agenda
'''

def conta_ocorrencias(agenda):
  dicionario = {}
  for nome in agenda: # Para cada nome "chave" na agenda...
    for telefone in agenda[nome]["telefones"]: # Para cada telefone na "agenda[nome]["telefones"]'
      if telefone not in dicionario:  # Se telefone não tiver no dicionário... adiciona e contabiliza 01 aparição.
        dicionario[telefone] = 1
      else:                           # Se ele não tiver no dicionário... soma mais 01 aparição.
        dicionario[telefone] += 1
  return dicionario

import unittest

agenda_testes1 = {
        'joao':22222222,
        'jose':33333333,
        }

#agendas melhoradas
agenda1 = {}
alfabeto  = 'abcde'
for c in alfabeto:
    agenda1[c] = {'telefones':[1122233344]} #uma agenda cujas pessoas sao as primeiras 5 letras
agenda2 = {}
vogais  = 'aeiouy'
for c in vogais:
    agenda2[c] = {'telefones':[11321321321]} #uma agenda cujas pessoas sao todas as vogais
agenda2['fulano'] = {'email':'fulano@exemplo.com', 'telefones':[1144440000]}
agenda3 = {}
pessoas = ['marcia','ana','marcos','heitor'] 
for p in pessoas:
    agenda3[p] = {'telefones':[1123232323]}
agenda3['fulano'] = {'email':'fulano@exemplo.com','telefones':[11777888999,1122222222]}

class TestPartOne(unittest.TestCase):

    def test_01_consulta(self):
        self.assertEqual(consulta(agenda_testes1,'joao'),22222222)
        self.assertEqual(consulta(agenda_testes1,'jose'),33333333)
    
    def test_02_adiciona(self):
        agenda_testes1 = {
           'joao':2,
           'jose':3,
        }
        adiciona(agenda_testes1,'marcia',55555555)
        self.assertEqual(consulta(agenda_testes1,'marcia'),55555555)
        adiciona(agenda_testes1,'antonio',88888888)
        self.assertEqual(consulta(agenda_testes1,'antonio'),88888888)
    
    def test_03_verifica(self):
        self.assertFalse(verifica(agenda_testes1,'marcia'))
        self.assertFalse(verifica(agenda_testes1,'antonio'))
        self.assertTrue(verifica(agenda_testes1,'joao'))
        self.assertTrue(verifica(agenda_testes1,'jose'))

      
    def test_04_conta_letras(self):
        self.assertEqual(conta_letras('banana'),{'b':1,'n':2,'a':3})
        self.assertEqual(conta_letras(''),{})
        self.assertEqual(conta_letras('a'*5+'b'*3+'c'*10+'a'),{'a':6,'b':3,'c':10})

    def test_05_email(self):
        self.assertEqual(email(agenda_melhor1,'lucas'),'lucas.goncalves@faculdadeimpacta.com.br')
        self.assertEqual(email(agenda_melhor1,'maria'),'maria.aparecida@exemplo.com')
        self.assertEqual(email(agenda2,'fulano'),'fulano@exemplo.com')
        self.assertEqual(email(agenda3,'fulano'),'fulano@exemplo.com')


    def test_06_telefone_principal(self):
        self.assertEqual(telefone_principal(agenda_melhor1,'lucas'),11999888999)
        self.assertEqual(telefone_principal(agenda_melhor1,'maria'),84999777444)
        self.assertEqual(telefone_principal(agenda_melhor1,'marta'),1177788899)
        self.assertEqual(telefone_principal(agenda1,'a'),1122233344)
        self.assertEqual(telefone_principal(agenda2,'a'),11321321321)
        self.assertEqual(telefone_principal(agenda3,'ana'),1123232323)
        self.assertEqual(telefone_principal(agenda3,'fulano'),11777888999)

    def test_07_sem_email(self):
        self.assertEqual(set(sem_email(agenda1)),set(list(alfabeto)))
        self.assertEqual(set(sem_email(agenda2)),set(list(vogais)))
        self.assertEqual(set(sem_email(agenda3)),set(pessoas))

    def test_08_conta_telefones(self):
        self.assertEqual(conta_telefones(agenda1),5)
        self.assertEqual(conta_telefones(agenda2),7)
        self.assertEqual(conta_telefones(agenda3),6)
    
    def test_09_conta_ocorrencias(self):
        self.assertEqual(conta_ocorrencias(agenda1),{1122233344:5})
        self.assertEqual(conta_ocorrencias(agenda2),{11321321321:6, 1144440000:1})
        self.assertEqual(conta_ocorrencias(agenda3),{1123232323:4, 11777888999:1,1122222222:1})


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
  from dicionarios_gabarito import *
except:
  pass

runTests()
