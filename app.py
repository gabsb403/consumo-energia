aparelho= input("Qual o aparelho?") 
potencia= input("Qual a potência?")
horasDia= input("Qual o tempo diário de uso em horas?")
consumo_mensal= (float(potencia) * float(horasDia) * 30) / 1000
print (f"aparelho: {aparelho}")
print (f" consumo estimado: {consumo_mensal:.2f} kWh/mês")