import random 
import hashlib



def passwd():
    print("\n")
    print("#####################################")
    lenght = input("Digite o tamanho que deseja para sua senha!: ")

    while lenght == "":
          lenght = input("Digite o tamanho que deseja para sua senha!: ")

          

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    number = '0123456789'
    caracter = '?!@#$%¨&*:;'

    all = lower + upper + number + caracter

    password = "".join(random.sample(all,int(lenght)))

    print(f"Sua senha: {password}")
    print("#####################################")


def criptografar():
      print("\n")
      password = input("Digite a senha que será criptografada: ")
      print("\n")
      algoritmo_de_criptografia = input("Digite o algoritmo de criptpgrafia: sha256 ou md5: ")
      
      if algoritmo_de_criptografia == "sha256":
           hash_object = hashlib.sha256()
      elif algoritmo_de_criptografia == "md5":
            hash_object = hashlib.md5()
      else:
           raise ValueError("Algoritimo de criptografia nao suportado!")
      
      hash_object.update(password.encode('utf-8'))
      return hash_object.hexdigest()

while True:
    print("\n")
    print("##################################")
    print("1 - Deseja cria uma senha?")
    print("2 - Deseja criptografar sua senha?")
    print("3 - Sair")

    escolha = input("Dijite a opção desejada: ")

    while escolha == "":
        escolha = input("Dijite a opção desejada: ")

    escolha = int(escolha)
        
    if escolha == 1:
        passwd()
    elif escolha == 2:
        print(f"Hash da senha: {criptografar()}")
    elif escolha == 3:
        break
