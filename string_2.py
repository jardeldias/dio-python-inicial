nome = "Jardel"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Jardel", "idade": 28}

# Forma antiga
print("Nome %s Idade %d" % (nome, idade))
print("Nome: {} idade {}".format(nome, idade))
print("Nome: {0} idade {1}".format(nome, idade))
print("Nome: {name} idade: {age}".format(name=nome, age=idade))

# Forma nova
print(f"Nome: {nome}, idade: {idade}")
