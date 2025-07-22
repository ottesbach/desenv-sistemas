Salario = float(input("Digite seu Salario:"))
Salarioanual = (Salario * 12)

if Salario > 5000:
  imposto_percentual = 0.08
else:
 imposto_percentual = 0.05

 imposto_mensal = Salario * imposto_percentual 
 imposto_anual = imposto_mensal * 12
 Salario_anual = Salario * 12

 print ("imposto mensal", imposto_mensal)
 print ("imposto anual", imposto_anual)
 print("Salario anual", Salario_anual)





