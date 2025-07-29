"""
4- Conversor de Temperatura 
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
# Solicitacção de dados do usuario (temperatura )
temperatura = float(input("Digite a temperatura: "))

# Solicitação da unidade de origem e unidade de destino
origem = input("Digite a unidade de origem (C para Celsius, F para  Fahrenheit, K para Kelvin): ")
destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ")

if origem == destino:
    resultado = temperatura

elif origem == "C": #origem Celsius
    if destino == "F": #origem Celsius para Fahrenheit      resultado = (temperatura * 9/5) + 32
        resultado = (temperatura * 9/5) + 32
    else: #origem Celsius para Kelvin
        resultado = temperatura + 273.15

elif origem == "F": #origem Fahrenheit
    if destino == "C": #origem Fahrenheit para Celsius
        resultado = (temperatura - 32) * 5/9 
    else: #origem Fahrenheit para Kelvin
        resultado = (temperatura - 32) * 5/9 + 273.15    
   
else: #origem Kelvin
    if destino == "C": #origem Kelvin para Celsius
        resultado = temperatura - 273.15
    else: #origem Kelvin para Fahrenheit
        resultado = (temperatura - 273.15) * 9/5 + 32   

# Exibição do resultado     
print(f"{temperatura} {origem} é igual a {resultado} {destino}")


