# def celsiusToFahrenheit(temp):
#     result = temp * 1.8 + 32
#     print(f"{temp} graus Celsius equivalem a {result} Fahrenheit.")

# temp = int(input("Digite a temperatura em graus Celsius: "))
# celsiusToFahrenheit(temp)

# nome = input("Insira seu nome completo com letras minúsculas: ")

def capitalizarNome(text):
    nome = text.split(' ')
    nome1=[]
    for word in nome:
        nome1.append(word.capitalize())
        
    
    return " ".join(nome1)
    
# print(nome.capitalize())
# print(f"Seu nome tem {len(nome)} letras.")
# print(nome.title())
print(capitalizarNome("lucas fortunato"))