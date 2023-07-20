# Tipos de dados em Python:
# Tipo inteiro (int):
a = 1
b = -2
c, d = (3, -4)

# Tipo string (str):
e = "Aydan"
f, g = ("Paulo", "Laís")

# Tipo float (float):
h = 1.5
i, j = (-2.833333, 23.86)

# Tipo boleano (bool):
k = True
ll = False
m, n = (False, True)

# dir() -> Sem argumentos, retorna a lista de nomes no escopo local atual:
dir()
dir(a)

# help() -> Sem argumentos, invoca o sistema de ajuda integrado:
help()
help(a)

# Para dados constantes, utiliza-se a convenção SCREMINGCASE:
VALOR = 30
PATH = "~/.ssh"

# Para dados variáveis, utiliza-se a convenção snake_case:
nome_aluno = "Aydan"
idade_aluno = 24
nota_aluno = 8.3

# Para converter valores, é necessário passar os contrutores ideais:

a = float(a)
# De float para int, todas as casas decimais serão ignoradas.
h = int(h)
idade_aluno = str(idade_aluno)
nota_aluno = str(nota_aluno)
nota_aluno = float(nota_aluno)

# Para consultar o tipo de uma variável, é utilizado a função type():
print(type(idade_aluno))
print(type(nota_aluno))
print(type(nome_aluno))

# Para inserção de dados, ultiliza-se a função input():
# Saída do tipo string!

nome_candidato = input("Insira o seu nome: ")
idade_candidato = input("Insira a sua idade: ")

# Para exibição de dados, ultiliza-se a função print():
# Há parâmetros especiais (end e sep)
print(nome_candidato, idade_candidato, end="?", sep=", #")

# Adição:
print(a + b)

# Subtração:
print(a - b)

# Multiplicação:
print(a * b)

# Divisão:
print(a / b)

# Divisão inteira:
print(a // b)

# Módulo:
print(a % b)

# Potenciação:
print(a ** b)

# Igualdade:
print(a == b)

# Diferença:
print(a != b)

# Maior/Maior ou igual:
print(a > b)
print(a >= b)

# Menor/Menor ou igual:
print(a < b)
print(a <= b)

# Atribuição:
o = 1

# Atribuição com soma:
o += 1
print(o)

# Atribuição com subtração:
o -= 1
print(o)

# Atribuição com multiplicação:
o *= 1
print(o)

# Atribuição com divisão:
o /= 1
print(o)

# Atribuição com divisão inteira:
o //= 1
print(o)

# Atribuição com módulo:
o %= 1
print(o)

# Atribuição com potenciação:
o **= 1
print(o)

# Operador lógico de união (and):

print(a > b and c == d)
print(a > b and c > d)

# Operador lógico de disjunção (or):

print(a > b and c == d)
print(a > b and c > d)

# Operador lógico de negação (not):
print(not a > b)

# Operador de identidade (is):
print(a is b)
print(a is not b)

# Operador de associação (in):
print(a in b)
print(a not in b)

# Iteração (for):

texto = input("Insira uma frase: \n>>> ")
VOGAIS = "AEIOU"

for i in texto:
    if i.upper() in VOGAIS:
        print(i)

# Iteração (range):
for i in range(0, 51, 5):
    print(i, end=", ")

p = "pYtHoN"
# Maiúsculas, minúsculas e título:
print(p.upper())
print(p.lower())
print(p.title())

# Eliminando espaços em branco:
q = "   Python  "
print(q.strip())
print(q.lstrip())
print(q.rstrip())

# Junções e centralização:
r = "Python"
print(r.center(10, "#"))
print(".".join(r))

# Interpolação de strings:
nome = "aydan barreto"
idade = 24
# 1° método:
print("Meu nome é %s e tenho %d anos." % (nome, idade))
# 2° método:
print("Meu nome é {} e tenho {} anos.", nome, idade)
# 3° método:
print("Meu nome é {} e tenho {} anos.".format(nome, idade))
# 4° método:
print(f"Meu nome é {nome} e tenho {idade} anos.")

# "Fatiamento" de strings:
print(nome[0])
print(nome[-1])
print(nome[:5])
print(nome[6:])
print(nome[6:13])
print(nome[6:13:2])
print(nome[:])
print(nome[::-1])

# String triplas (múltiplas linhas):
# Preserva a formatação da string

mensagem = f"""Olá, meu nome é {nome},
                tenho {idade} anos e 
                quero ganhar 5 dígitos
                por mês."""
print(mensagem)


